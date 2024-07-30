"""Module for control over the 
KIPRIM DC310S power supply unit.

https://github.com/maximweb/kiprim-dc310s
"""

import serial
from enum import Enum

class GetPSU(Enum):
    device_info= "*idn?"
    is_active= "output?"
    measured_i= "measure:current?"
    measured_v= "measure:voltage?"
    set_i= "current?"
    set_v= "voltage?"
    limit_i= "current:limit?"
    limit_v= "voltage:limit?"
    
class SetPSU(Enum):
    on= "output 1"
    off= "output 0"
    current= "current "
    voltage= "voltage "
    limit_i= "current:limit "  # followed by float
    limit_v= "voltage:limit "  # followed by float

class PowerSupply:
    """Class for control over KIPRIM DC310S"""
    def __init__(self, port):
        self.serial = serial.Serial(port=port, baudrate=115200, timeout=1)
    
    def get_device_info(self):
        self._write(GetPSU.device_info.value)
        return self._read()
    
    def get_is_active(self):
        self._write(GetPSU.is_active.value)
        return self._read()
    
    def get_measured_current(self):
        self._write(GetPSU.measured_i.value)
        return self._read()
    
    def get_measured_voltage(self):
        self._write(GetPSU.measured_v.value)
        return self._read()
    
    def get_set_current(self):
        self._write(GetPSU.set_i.value)
        return self._read()
    
    def get_set_voltage(self):
        self._write(GetPSU.set_v.value)
        return self._read()
    
    def get_limit_current(self):
        self._write(GetPSU.limit_i.value)
        return self._read()
    
    def get_limit_voltage(self):
        self._write(GetPSU.limit_v.value)
        return self._read()
    
    def turn_on(self):
        self._write(SetPSU.on.value)
        
    def turn_off(self):
        self._write(SetPSU.off.value)
        
    def set_current(self, current: float):
        self._write(SetPSU.current.value + str(current))
        
    def set_voltage(self, voltage: float):
        self._write(SetPSU.voltage.value + str(voltage))
    
    def set_limit_current(self, current: float):
        self._write(SetPSU.limit_i.value + str(current))
        
    def set_limit_voltage(self, voltage: float):
        self._write(SetPSU.limit_v.value + str(voltage))
    
    def _write(self, command: str):
        """Write a command to the power supply,
        encoded as bytes with a trailing newline character.
        """
        self.serial.write(command.encode() + b"\n")
        
    def _read(self):
        """Read the response from the power supply,
        converting to a float if possible.
        """
        string = self.serial.readline().decode().strip()
        try:
            return float(string)
        except ValueError:
            return string
    
    def __del__(self):
        self.serial.close()
