from .powersupply import PowerSupply
from .ssr import SSRPulser
from WF_SDK import device, pattern
from enum import Enum

class State(Enum):
    PULSE = 1
    TAPER = 2
    NEUTRAL = 3
    DISCHARGE = 4
    
class StateController:
    """Hardware controller for state switching"""
    def __init__(self, psu_com, psu_set_v, psu_set_i, pin_ssr_chg, pin_ssr_dis):
        
        self.dev = device.open()
        self.ssr_c = SSRPulser(self.dev, pin_ssr_chg)
        self.ssr_d = SSRPulser(self.dev, pin_ssr_dis)
        self.psu = PowerSupply(psu_com)
        self.neutral()
        
        self.psu.set_limit_voltage(psu_set_v + 1)
        self.psu.set_limit_current(psu_set_i + 0.1)
        self.psu.set_voltage(psu_set_v)
        self.psu.set_current(psu_set_i)
        
    def neutral(self):
        """Idle safe state"""
        self.psu.turn_off()
        self.ssr_c.shut()
        self.ssr_d.shut()
        self.state = State.NEUTRAL
        
    def pulse(self, freq, duty):
        """Pulse charge"""
        self.psu.turn_on()
        self.ssr_c.pulse(freq, duty)
        self.ssr_d.shut()
        self.state = State.PULSE
        
    def taper(self):
        """Taper charge"""
        self.psu.turn_on()
        self.ssr_c.open()
        self.ssr_d.shut()
        self.state = State.TAPER
        
    def discharge(self):
        """Discharge"""
        self.psu.turn_off()
        self.ssr_c.shut()
        self.ssr_d.open()
        self.state = State.DISCHARGE
    
    def __del__(self):
        self.neutral()
        pattern.close(self.dev)
        device.close(self.dev)