


if __name__ == "__main__":
    from constants import *
    from controllers.ssr import SSRPulser
    from controllers.daq import DAQ
    from controllers.powersupply import PowerSupply
    from WF_SDK import device, pattern
    from constants import *
    import time
    
    # Init devices
    dev = device.open()
    ssr_charge = SSRPulser(dev, SSR_CHARGE_PIN)
    ssr_discharge = SSRPulser(dev, SSR_DISCHARGE_PIN)
    daq = DAQ(SHUNT_PIN1, SHUNT_PIN2, 1)
    psu = PowerSupply(port=PSU_PORT)
    
    def read():
        """Returns measurements 
        of current & volt as tuple
        """
        return daq.read_shunt_current(SAMPLE_INTERVAL, SHUNT_NOISE_THRESH), daq.read_battery_voltage()

    def shutdown():
        """Shuts down devices and exits"""
        ssr_charge.shut()
        ssr_discharge.shut()
        psu.turn_off()
        pattern.close(dev)
        device.close(dev)
        exit()
    
    # Initial (shutoff) state
    ssr_charge.shut()
    ssr_discharge.shut()
    psu.turn_off()
    psu.set_limit_current(BATT_I_CH + 0.1)
    psu.set_limit_voltage(BATT_V_HI + 1)
    psu.set_current(BATT_I_CH)
    psu.set_voltage(BATT_V_HI)
    
    try:
        # Begin
        psu.turn_on()
        c,v = read()
    
        # Pulse charge (CC) 
        ssr_discharge.shut()
        ssr_charge.open()  # FIXME pulse
        while psu.get_measured_voltage() < BATT_V_HI:
            print(c, v)
            c, v = read()
        
        # Taper charge (CV)
        ssr_discharge.shut()
        ssr_charge.open()
        while c > TC_CUTOFF_I:
            print(c, v)
            c, v = read()
            
        # Discharge
        ssr_charge.shut()
        psu.turn_off()
        ssr_discharge.open()
        while v > BATT_V_LO:
            print(c, v)
            c, v = read()
            
    except KeyboardInterrupt:
        shutdown()
    shutdown()
    

# # User Parameters # FIXME un-hardcode
# PSU_PORT          = str()    #       COM port for PSU
# CSV_PATH          = str()    #       Path to save data
# SHUNT_RESISTANCE  = float()  # (Ohms)
# BATT_I_CHARGE     = float()  # (A)   CC setpoint
# BATT_V_HI         = float()  # (V)   CC cutoff cond, CV setpoint
# BATT_I_LO         = float()  # (A)   CV cutoff cond
# BATT_V_LO         = float()  # (V)   Discharging cutoff cond
# CYCLE_T_MAX       = float()  # (hr)  Abort cond (per any battery cycle)
# CHARGE_T_MAX      = float()  # (hr)  Abort cond (in charge step)
# CAPACITY_LO_PCENT = float()  # (%)   Abort cond (in discharge step)
# PULSE_FREQ        = float()  # (Hz)
# PULSE_DUTY        = float()  # (%)
# SAMPLE_INTERVAL   = float()  # (s)