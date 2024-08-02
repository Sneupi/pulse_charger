"""Controllers related to the DAQ unit used in the pulse charging system
"""

import nidaqmx  # using the NI DAQ USB-6008

class DAQInput:
    """Class for reading the voltage of two 
    different pins, each relative to ground"""
    def __init__(self, d_in1: int, d_in2: int):
        self.task = nidaqmx.Task()
        self.task.ai_channels.add_ai_voltage_chan(f"Dev1/ai{d_in1}")
        self.task.ai_channels.add_ai_voltage_chan(f"Dev1/ai{d_in2}")
        self.task.start()
    
    def read_v1(self):
        """Read the voltage on line 1 relative to ground"""
        return self.task.read()
    
    def read_v2(self):
        """Read the voltage on line 2 relative to ground"""
        return self.task.read()
    
    def __del__(self):
        self.task.stop()
        self.task.close()
        
class PulseChargeDAQ(DAQInput):
    """Class for reading necessary circuit values from the DAQ unit"""
    def __init__(self, d_in1: int, d_in2: int, resistance: float):
        """
        Args:
            d_in1 (int): Pin before the shunt resistor
            d_in2 (int): Pin after the shunt resistor
            resistance (float): Resistance (Ohms) of the shunt resistor
        """
        super().__init__(d_in1, d_in2)
        self.resistance = resistance
    
    def read_battery_voltage(self):
        """Read the circuit voltage between 
        ground and after the shunt resistor"""
        return self.read_v2()
    
    def read_shunt_current(self):
        """Read the current through the shunt resistor"""
        return (self.read_v2() - self.read_v1()) / self.resistance
    