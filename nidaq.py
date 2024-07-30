"""Controller for openning and closing the 
discharge SSR (Solid State Relay)
and analog Data Acquisition (DAQ) 
for main pulse charge control
"""

import nidaqmx
from nidaqmx.constants import LineGrouping

class LineControl:
    """Class for controlling the digital 
    output of one line on the DAQ"""
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
    