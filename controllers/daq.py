"""Controllers related to the DAQ unit used in the pulse charging system
"""

import nidaqmx  # using the NI DAQ USB-6008
import time

class DAQ:
    """Class for reading the voltage of two 
    different pins, each relative to ground"""
    def __init__(self, d_in1: int, d_in2: int):
        self.task = nidaqmx.Task()
        self.task.ai_channels.add_ai_voltage_chan(f"Dev1/ai{d_in1}")
        self.task.ai_channels.add_ai_voltage_chan(f"Dev1/ai{d_in2}")
        self.task.start()
    
    def read_v1(self):
        """Read the voltage on line 1 relative to ground"""
        return self.task.read()[0] + 1.4  # offset bc RSE mode
    
    def read_v2(self):
        """Read the voltage on line 2 relative to ground"""
        return self.task.read()[1] + 1.4  # offset bc RSE mode
    
    def read_vdiff(self):
        """Read the voltage difference between the two lines"""
        return self.read_v2() - self.read_v1()
    
    def read_vdiff(self, sampling_interval: float, noise_thresh: float):
        """Returns the average voltage difference between the two lines
        over the given reading interval (seconds), 
        ignoring readings below the noise threshold."""
        t = time.time()
        data = []
        # Read as many points as possible within interval
        while time.time() - t < sampling_interval:
            pt = self.read_v2() - self.read_v1()
            # Ignore readings below noise threshold
            if pt < noise_thresh:
                continue
            data.append(pt)
        return sum(data) / len(data) if len(data) else 0.0
    
    def __del__(self):
        self.task.stop()
        self.task.close()