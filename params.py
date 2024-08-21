"""Run parameters for the current 
session of battery pulse charge cycler"""

import printing as term_print

# PSU_PORT           
# SHUNT_RESISTANCE   # Ohms
# SHUNT_NOISE_THRESH # A
# CSV_PATH           
# SAMPLE_INTERVAL    # s
# BATT_V_HI          # V, battery max op
# BATT_V_LO          # V, battery min op
# STANDING_TIME      # s, idling time after tc
# CHG_CURRENT        # A, charging amperage
# TC_CUTOFF_I        # A, taper charge low cutoff
# CAP_PCENT_EXIT     # %, exit cycling at this % of initial capacity
# PULSE_FREQ         # Hz, pulse frequency
# PULSE_DUTY         # %, pulse duty cycle
# PC_TIMEOUT         # s, pulse charge timeout
# TC_TIMEOUT         # s, taper charge timeout

try: 
    PSU_PORT           = str(input("Enter the PSU port: "))
    SHUNT_RESISTANCE   = float(input("Enter the shunt resistance (Ohms): "))
    CSV_PATH           = str(input("Enter the CSV path: "))
    SAMPLE_INTERVAL    = float(input("Enter the sample interval (sec): "))
    BATT_V_HI          = float(input("Enter the battery upper voltage lim (V): "))
    BATT_V_LO          = float(input("Enter the battery low voltage lim (V): "))
    STANDING_TIME      = float(input("Enter the standing time after taper charge (sec): "))
    CHG_CURRENT        = float(input("Enter the charging current (Amps): "))
    TC_CUTOFF_I        = float(input("Enter the taper charge cutoff current (Amps): "))
    CAP_PCENT_EXIT     = float(input("Enter the capacity percent exit (0.0 to 1.0): "))
    PULSE_FREQ         = int(input("Enter the pulse frequency (Hz): "))
    PULSE_DUTY         = int(input("Enter the pulse duty cycle (0 to 100): "))
    PC_TIMEOUT         = int(input("Enter the pulse charge timeout (sec): "))
    TC_TIMEOUT         = int(input("Enter the taper charge timeout (sec): "))
except ValueError as e:
    term_print.exception(e)
    exit()
except KeyboardInterrupt:
    term_print.kb_interrupt()
    exit()