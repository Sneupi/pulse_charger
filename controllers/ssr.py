"""Controller for the Solid State Relays (SSR) used in the pulse charging system"""

from .pulsegenerator import PulseGenerator

class SSRPulser:
    """Class for controlling the Solid State Relays (SSR)
    with 3 different modes: open, shut, pulsed"""
    def __init__(self, device_data, pin):
        """
        Args:
            device_data (Any): Digilent Digital Discovery device data
            pin (int): Digital Out pin number
            freq (int): Frequency of the pulse signal
            duty (int): Duty cycle of the pulse signal
        """
        self.pin = PulseGenerator(device_data, pin)
        
    def open(self):
        """Pull the pin constant up"""
        self.pin.run(1, 100)  # 100% duty aka ON
    
    def shut(self):
        """Pull the pin constant down"""
        self.pin.run(1, 0)  # 0% duty aka OFF
    
    def pulse(self, frequency, duty_cycle):
        """Generate waveform pattern on the pin"""
        self.pin.run(frequency, duty_cycle)
        
# if __name__ == "__main__":
#     # Example usage
#     from WF_SDK import device, pattern
#     import time
#     device_data = device.open()
    
#     ssr1 = SSRPulser(device_data, pin=27)
#     ssr2 = SSRPulser(device_data, pin=26)
    
#     while True:
#         try:
#             ssr1.open()
#             ssr2.shut()
#             time.sleep(5)
#             ssr1.shut()
#             ssr2.pulse(1000, 50)
#             time.sleep(5)
#             ssr1.pulse(2500, 75)
#             ssr2.open()
#             time.sleep(5)
#         except KeyboardInterrupt:
#             break
        
#     pattern.close(device_data)
#     device.close(device_data)