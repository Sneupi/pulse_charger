"""Initialization procedures for the pulse charge system"""

from controllers.daq import DAQ       # Voltage & current reader
from controllers.powersupply import PowerSupply  # PSU Controller
from controllers.ssr import SSRPulser            # Relay(s) Controller

def psu(psu: PowerSupply):
    """Power supply init procedure. Asserts
    system is completely off."""
    psu.turn_off()
    assert psu.get_measured_voltage() == 0, \
        f"Voltage should be 0: {psu.get_measured_voltage()}"
    assert psu.get_measured_current() == 0, \
        f"Current should be 0: {psu.get_measured_current()}"
    
def ssrs(charge_ssr: SSRPulser, discharge_ssr: SSRPulser):
    """SSR(s) init procedure. Sets both SSRs to off state."""
    charge_ssr.shut()
    discharge_ssr.shut()
    
def daq(daq: DAQ):
    """Shunt reader init procedure"""
    assert daq.read_battery_voltage() == 0, f"Voltage should be 0: {daq.read_battery_voltage()}"
    assert daq.read_shunt_current() == 0, f"Current should be 0: {daq.read_shunt_current()}"
    
