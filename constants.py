"""Constants used to initialize controller 
instances for the DAQ and SSR devices in 
the main pulse charge control system"""

# Diligent Digital Discovery
SSR_CHARGE_PIN = 33
SSR_DISCHARGE_PIN = 32

# NI USB-6001 DAQ
SHUNT_PIN1 = 0  # ai0
SHUNT_PIN2 = 1  # ai1

# SHUNT
SHUNT_RESISTANCE = 1  # Ohms
SHUNT_NOISE_THRESH = 0.01  # Amps

# READINGS
SAMPLE_INTERVAL = 5  # seconds

# BATTERY LIMITS
BATT_V_LO = 2.7  # Volts