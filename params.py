"""Run parameters for the current 
session of battery pulse charge cycler"""

PSU_PORT = str()
SHUNT_RESISTANCE = float()      # Ohms
SHUNT_NOISE_THRESH = float()    # A
CSV_PATH = str
SAMPLE_INTERVAL = float()       # s
BATT_V_HI = float()             # V, battery max op
BATT_V_LO = float()             # V, battery min op
STANDING_TIME = float()         # s, idling time after tc
CHG_CURRENT = float()           # A, charging amperage
TC_CUTOFF_I = float()           # A, taper charge low cutoff
CAP_PCENT_EXIT = float()        # %, exit cycling at this % of initial capacity
PULSE_FREQ = int()              # Hz, pulse frequency
PULSE_DUTY = int()              # %, pulse duty cycle
PC_TIMEOUT = int()              # s, pulse charge timeout
TC_TIMEOUT = int()              # s, taper charge timeout

def get_input():
    global PSU_PORT, SHUNT_RESISTANCE, SHUNT_NOISE_THRESH, CSV_PATH, \
    SAMPLE_INTERVAL, BATT_V_HI, BATT_V_LO, STANDING_TIME, CHG_CURRENT, \
    TC_CUTOFF_I, CAP_PCENT_EXIT, PULSE_FREQ, PULSE_DUTY, PC_TIMEOUT, TC_TIMEOUT
    
    PSU_PORT = input("Enter the PSU port: ")
    SHUNT_RESISTANCE = float(input("Enter the shunt resistance (Ohms): "))
    SHUNT_NOISE_THRESH = float(input("Enter the shunt noise threshold (Amps): "))
    CSV_PATH = input("Enter the CSV path: ")
    SAMPLE_INTERVAL = float(input("Enter the sample interval (sec): "))
    BATT_V_HI = float(input("Enter the battery upper voltage lim (V): "))
    BATT_V_LO = float(input("Enter the battery low voltage lim (V): "))
    STANDING_TIME = float(input("Enter the standing time after taper charge (sec): "))
    CHG_CURRENT = float(input("Enter the charging current (Amps): "))
    TC_CUTOFF_I = float(input("Enter the taper charge cutoff current (Amps): "))
    CAP_PCENT_EXIT = float(input("Enter the capacity percent exit (0.0 to 1.0): "))
    PULSE_FREQ = int(input("Enter the pulse frequency (Hz): "))
    PULSE_DUTY = int(input("Enter the pulse duty cycle (0-100%): "))
    PC_TIMEOUT = int(input("Enter the pulse charge timeout (sec): "))
    TC_TIMEOUT = int(input("Enter the taper charge timeout (sec): "))