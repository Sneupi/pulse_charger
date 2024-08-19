"""Constants used to initialize controller 
instances for the DAQ and SSR devices in 
the main pulse charge control system"""

# Diligent Digital Discovery
SSR_CHARGE_PIN = 33
SSR_DISCHARGE_PIN = 32

# NI USB-6001 DAQ
SHUNT_PIN1 = 0  # ai0
SHUNT_PIN2 = 1  # ai1

# PSU
PSU_PORT = "COM15"

# SHUNT
SHUNT_RESISTANCE = 1  # Ohms
SHUNT_NOISE_THRESH = 0.01  # Amps

# READINGS
CSV_PATH = "data.csv"
SAMPLE_INTERVAL = 5  # seconds

# BATTERY LIMITS
BATT_V_HI   = 4.2               # V, battery max op
BATT_V_LO   = 3.6               # V, battery min op

# RUN PARAMETERS
STANDING_TIME = 11             # s, idling time after tc
CHG_CURRENT   = 170            # mA, charging amperage
TC_CUTOFF_I   = 130            # mA, taper charge low cutoff
CAP_PCENT_EXIT = .7             # %, exit cycling at this % of initial capacity
PULSE_FREQ    = 100            # Hz, pulse frequency
PULSE_DUTY    = 50              # %, pulse duty cycle
PC_TIMEOUT    = 3600              # s, pulse charge timeout
TC_TIMEOUT    = 3600              # s, taper charge timeout
SSR_INPUT_V   = 3.3             # V, SSR input voltage
SSR_INPUT_I   = 16             # mA, SSR input current
assert TC_CUTOFF_I > SHUNT_NOISE_THRESH, "Taper charge cutoff current must be above current noise threshold"