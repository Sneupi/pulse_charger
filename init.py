"""Initialization procedures for the pulse charge system"""

from controllers.daq import DAQ       # Voltage & current reader
from controllers.powersupply import PowerSupply  # PSU Controller
from controllers.ssr import SSRPulser            # Relay(s) Controller
from constants import *                          # Parameters

def psu(psu: PowerSupply):
    """Power supply init procedure. Asserts
    system is completely off."""
    psu.turn_off()
    psu.set_limit_current(CHG_CURRENT + 0.1)
    psu.set_limit_voltage(BATT_V_HI + 1)
    psu.set_current(CHG_CURRENT)
    psu.set_voltage(BATT_V_HI)
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
    v = daq.read_battery_voltage()
    assert v == 0, f"Voltage should be 0: {v}"
    i = daq.read_shunt_current(SAMPLE_INTERVAL, SHUNT_NOISE_THRESH)
    assert i == 0, f"Current should be 0: {i}"
    
