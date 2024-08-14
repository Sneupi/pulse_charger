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
PSU_PORT = "COM14"

# SHUNT
SHUNT_RESISTANCE = 1  # Ohms
SHUNT_NOISE_THRESH = 0.01  # Amps

# READINGS
CSV_PATH = "data.csv"
SAMPLE_INTERVAL = 5  # seconds

# BATTERY LIMITS
BATT_V_HI   = 4.2               # V, battery max op
BATT_V_LO   = 2.7               # V, battery min op

# RUN PARAMETERS
STANDING_TIME = 120             # s, idling time after tc
CHG_CURRENT   = 0.17            # A, charging amperage
TC_CUTOFF_I   = 0.03            # A, taper charge low cutoff

assert TC_CUTOFF_I > SHUNT_NOISE_THRESH, "Taper charge cutoff current must be above current noise threshold"