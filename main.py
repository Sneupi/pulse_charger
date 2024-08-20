
from constants import *
from controllers.daq import DAQ
from logger import Logger
from constants import *
from controllers.state import StateController, State
import time
import printing as term_print
from threading import Timer

class PulseChargeException(Exception):
    pass
class TaperChargeException(Exception):
    pass

logger = Logger(CSV_PATH)
daq = DAQ(SHUNT_PIN1, SHUNT_PIN2)
ctrl = StateController(PSU_PORT, BATT_V_HI, CHG_CURRENT, 
                        SSR_CHARGE_PIN, SSR_DISCHARGE_PIN)

def read_current():
    """Current through shunt resistor
    
    WARNING: blocking for SAMPLE_INTERVAL seconds"""
    return daq.read_vdiff(SAMPLE_INTERVAL, SHUNT_NOISE_THRESH) / SHUNT_RESISTANCE

def read_v_bat():
    """Voltage of the battery"""
    return daq.read_v2()

def read_v_psu():
    """Voltage of the power supply"""
    return ctrl.psu.get_measured_voltage()

def get_dQ(mA, sec):
    """Gets mAh over step interval"""
    return mA * (sec / 3600)

def get_dt(t_beg, t_end):
    """Gets the time elapsed in seconds"""
    return t_end - t_beg

try: 
    cycle_number = 0
    mAh_initial = None
    term_print.begin(cycle_number)
    
    while (mAh_initial is None) or (mAh > mAh_initial * CAP_PCENT_EXIT):
        mAh = 0
        t_pulse = None
        t_taper = None
        
        # First state
        term_print.pulse()
        ctrl.pulse(PULSE_FREQ, PULSE_DUTY)
        t_pulse = time.time()
        
        # State machine
        while True:
            
            # Measure
            t_beg = time.time()
            amps, v_bat, v_psu = read_current(), read_v_bat(), read_v_psu()
            t_end = time.time()
            mA = amps * 1000
            dt = get_dt(t_beg, t_end)
            dQ = get_dQ(mA, dt)
            
            # Log & Print
            logger.log(cycle_number, dt, mA, v_bat, v_psu, dQ)
            term_print.stats(cycle_number, dt, mA, v_bat, v_psu, dQ)
            
            # If discharging, do mAh sum
            if ctrl.state == State.DISCHARGE:
                mAh += abs(dQ)
            
            # State-based control
            match ctrl.state:
                case State.PULSE:
                    # Transition
                    if amps < CHG_CURRENT - SHUNT_NOISE_THRESH: 
                        term_print.taper()
                        ctrl.taper()
                        t_taper = time.time()  
                    # Timeout
                    elif time.time() - t_pulse >= PC_TIMEOUT:
                        raise PulseChargeException("Timeout")
                        
                case State.TAPER:
                    # Transition
                    if amps <= TC_CUTOFF_I:  
                        term_print.stand(STANDING_TIME)
                        ctrl.neutral()
                        # Transitions to discharge after standing
                        Timer(STANDING_TIME, lambda: term_print.discharge() or ctrl.discharge()).start()
                    # Timeout
                    elif time.time() - t_taper >= TC_TIMEOUT:
                        raise TaperChargeException("Timeout")
                    
                case State.DISCHARGE:
                    # Transition
                    if v_bat <= BATT_V_LO:  
                        break
        
        # End of cycle
        if mAh_initial is None:
            mAh_initial = mAh
        cycle_number += 1
    
    # Exit Program
    term_print.exit_ok()
       
except KeyboardInterrupt:
    term_print.kb_interrupt()
    
except Exception as e:
    term_print.exception(e)
    
finally:
    ctrl.neutral()
    input("(PRESS ENTER TO CLOSE)")