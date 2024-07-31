"""Controller for openning and closing the 
discharge SSR (Solid State Relay)
and analog Data Acquisition (DAQ) 
for main pulse charge control
"""

import nidaqmx
from nidaqmx.constants import LineGrouping

class DAQOutput:
    """Class for switching a digital 
    output line on the DAQ"""
    def __init__(self, port: int, line: int):
        self.task = nidaqmx.Task()
        self.task.do_channels.add_do_chan(f"Dev1/port{port}/line{line}", 
                                          line_grouping=LineGrouping.CHAN_PER_LINE)
        self.task.start()
        self.task.write(False)
        
    def enable(self):
        self.task.write(True)
        
    def disable(self):
        self.task.write(False)
        
    def __del__(self):
        self.task.stop()
        self.task.close()
    
class DAQInput:
    """Class for reading voltage 
    between two analog DAQ lines"""
    def __init__(self, line1: int, line2: int):
        self.task = nidaqmx.Task()
        self.task.ai_channels.add_ai_voltage_chan(f"Dev1/ai{line1}")
        self.task.ai_channels.add_ai_voltage_chan(f"Dev1/ai{line2}")
        self.task.start()
    
    def read(self):
        v1, v2 = self.task.read()
        return (v1-v2)
    
    def __del__(self):
        self.task.stop()
        self.task.close()

    