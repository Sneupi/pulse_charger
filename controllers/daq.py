"""Controllers related to the DAQ unit used in the pulse charging system
"""

import nidaqmx  # using the NI DAQ USB-6008
import time

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
        return self.task.read()[0]
    
    def read_v2(self):
        """Read the voltage on line 2 relative to ground"""
        return self.task.read()[1]
    
    def __del__(self):
        self.task.stop()
        self.task.close()
        
class DAQ(DAQInput):
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
        return self.read_v2() + 1.4  # 1.4V offset NI USB-6008 in RSE
    
    def _read_shunt_current(self):
        """Read the current through the shunt resistor"""
        return abs(self.read_v2() - self.read_v1()) / self.resistance
    
    def read_shunt_current(self, sampling_interval: float, noise_thresh: float):
        """Returns the average current through the 
        shunt resistor over the given reading interval (seconds),
        ignoring readings below the noise threshold."""
        t = time.time()
        data = []
        # Read as many points as possible within interval
        while time.time() - t < sampling_interval:
            pt = self._read_shunt_current()
            # Ignore readings below noise threshold
            if pt < noise_thresh:
                continue
            data.append(self._read_shunt_current())
        return sum(data) / len(data) if len(data) else 0