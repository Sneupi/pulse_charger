


if __name__ == "__main__":
    from constants import *
    from controllers.ssr import SSRPulser
    from controllers.daq import DAQ
    from WF_SDK import device, pattern
    from constants import *
    import time
    
    dev = device.open()
    ssr_charge = SSRPulser(dev, SSR_CHARGE_PIN)
    ssr_discharge = SSRPulser(dev, SSR_DISCHARGE_PIN)
    daq = DAQ(SHUNT_PIN1, SHUNT_PIN2, 1)
    break_flag = False
    
    # ssr_charge.pulse(1, 75)
    # try:
    #     while True:
    #         print(daq.read_shunt_current(SAMPLE_INTERVAL, SHUNT_NOISE_THRESH))
    #         if break_flag:
    #             break
    # except KeyboardInterrupt:
    #     break_flag = True
    
    # ssr_charge.shut()
    # ssr_discharge.open()
    # try:
    #     while daq.read_battery_voltage() > BATT_V_LO:
    #         print(daq.read_battery_voltage())  # FIXME testing
    #         time.sleep(SAMPLE_INTERVAL)
    #         if break_flag:
    #             break
    # except KeyboardInterrupt:
    #     break_flag = True

    # testing ssr switch frequency rating
    try:
        ssr_discharge.pulse(100, 50)
        while True:
            time.sleep(1)
            if break_flag:
                break
    except KeyboardInterrupt:
        break_flag = True
        
    ssr_charge.shut()
    ssr_discharge.shut()
    pattern.close(dev)
    device.close(dev)
    exit()



# from controllers.daq import DAQ       # Shunt & battery DAQ
# from controllers.powersupply import PowerSupply  # PSU control
# from controllers.ssr import SSRPulser            # Relay(s) control
# from constants import *                          # Device pins
# from WF_SDK import device, pattern               # drivers for Digilent (the SSR controller)
# import init                                      # Init procedures
# from recorder import Recorder                    # Data recording

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

# DEBUG = True

# # Controllers
# diligent = device.open()
# charge_ssr = SSRPulser(diligent, pin=SSR_CHARGE_PIN)
# discharge_ssr = SSRPulser(diligent, pin=SSR_DISCHARGE_PIN)
# psu = PowerSupply(port=PSU_PORT)
# daq = DAQ(SHUNT_PIN1, SHUNT_PIN2, SHUNT_RESISTANCE)
# recorder = Recorder(daq, CSV_PATH, interval=SAMPLE_INTERVAL)

# # Globals
# capactiy = 0  # (mAh) Running total of accumulated capacity

# # Init Procedures
# init.ssrs(charge_ssr, discharge_ssr)
# init.psu(psu)
# init.daq(daq)

# # TODO main loop here

# # Cleanup procedure
# charge_ssr.shut()
# discharge_ssr.shut()
# psu.turn_off()
# recorder.stop()
# pattern.close(diligent)    
# device.close(diligent)
