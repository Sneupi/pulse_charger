"""Recording module for voltage and current data"""

from controllers.daq import PulseChargeDAQ
import csv
import time

class Recorder:
    """Class for periodically recording battery voltage and current data"""
    def __init__(self, daq: PulseChargeDAQ, path: str, interval: float):
        """
        Args:
            daq (PulseChargeDAQ): DAQ unit for reading voltage and current
            path (str): Path to save the CSV file
            interval (float): Seconds interval between each time point
        """
        self.daq = daq
        self.path = path
        self.interval = interval
        
    def start(self):
        raise Exception("# TODO")
    
    def stop(self):
        raise Exception("# TODO")