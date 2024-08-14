
from constants import *
from controllers.daq import DAQ
from controllers.powersupply import PowerSupply
from logger import Logger
from constants import *
from controllers.state import StateController
import time
import init

BLUE = '\033[34m'
WHITE = '\033[37m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RED = '\033[31m'

# Init devices
logger = Logger(CSV_PATH)
daq = DAQ(SHUNT_PIN1, SHUNT_PIN2)
psu = PowerSupply(PSU_PORT)
state = StateController(psu, SSR_CHARGE_PIN, SSR_DISCHARGE_PIN)
init.psu(psu)
init.daq(daq)

def read():
    return abs(daq.read_vdiff(SAMPLE_INTERVAL, SHUNT_NOISE_THRESH))/SHUNT_RESISTANCE, daq.read_v2()

def process(c,v):
    """Processes current & voltage readings"""
    global mAh_curr
    c = round(c, 3) * 1000
    v = round(v, 3)
    mAh_step = c * SAMPLE_INTERVAL / 3600
    mAh_curr += mAh_step
    logger.log(c, v, mAh_step, mAh_curr)
    print(f"{BLUE}I: {c:.01f}mA  |  V: {v:.03f}V  |  Step: {mAh_step:.04f}mAh  |  Sum: {mAh_curr:.04f}mAh{WHITE}")
    
mAh_init = 0
mAh_curr = 0
c, v = read()

try:
    print(f"{GREEN}BEGIN CYCLING{WHITE}")
    
    while mAh_curr >= mAh_init * CAP_PCENT_EXIT:
        
        print(f"{GREEN}PULSE CHARGING...{WHITE}")
        state.pulse(PULSE_FREQ, PULSE_DUTY)
        time.sleep(2)
        while psu.get_measured_current() > CHG_CURRENT:
            c,v = read()
            process(c,v)
            
        print(f"{GREEN}TAPER CHARGING...{WHITE}")
        state.taper()
        c,v = read()
        process(c,v)
        while c > TC_CUTOFF_I:
            c,v = read()
            process(c,v)
        
        print(f"{GREEN}STANDING FOR {STANDING_TIME} SEC...{WHITE}")
        state.neutral()
        t = time.time()
        while time.time() - t < STANDING_TIME:
            c, v = read()
            process(c,v)
        
        print(f"{GREEN}DISCHARGING...{WHITE}")
        state.discharge()
        while v > BATT_V_LO:
            c,v = read()
            process(c,v)
        
        if mAh_init == 0:
            mAh_init = mAh_curr
    print(f"{GREEN}EXITED WITHOUT INTERRUPT{WHITE}")
       
except KeyboardInterrupt:
    print(f"{YELLOW}EXITING FROM CTRL+C{WHITE}")
    
except Exception as e:
    print(f"{RED}UNHANDLED EXCEPTION:\n{e}{WHITE}")
    
del state
del psu
del daq
del logger