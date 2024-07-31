
from pulsegenerator import PulseGenerator

class SSRPulser:
    """Encapsulates control of a Solid State Relay (SSR) 
    in pulse charging system, which has 3 states of 
    operation: off, on, and square wave. Using the 
    Diligent Digital Discovery device as the hardware unit.
    """
    def __init__(self, device_data, pin, freq, duty):
        """
        Args:
            device_data (Any): Digilent Digital Discovery device data
            pin (int): Digital Out pin number
            freq (int): Frequency of the pulse signal
            duty (int): Duty cycle of the pulse signal
        """
        self.pin = PulseGenerator(device_data, pin)
        self.frequency = freq
        self.duty_cycle = duty
        
    def set_state_on(self):
        """Pull the pin up"""
        self.pin.run(1, 100)  # 100% duty aka ON
    
    def set_state_off(self):
        """Pull the pin down"""
        self.pin.run(1, 0)  # 0% duty aka OFF
    
    def set_state_pulse(self):
        """Generate waveform pattern on the pin"""
        self.pin.run(self.frequency, self.duty_cycle)
        
# if __name__ == "__main__":
#     # Example usage
#     from WF_SDK import device, pattern
#     import time
#     device_data = device.open()
    
#     ssr1 = SSRPulser(device_data, pin=27, freq=2500, duty=75)
#     ssr2 = SSRPulser(device_data, pin=26, freq=1000, duty=50)
    
#     while True:
#         try:
#             ssr1.set_state_on()
#             ssr2.set_state_off()
#             time.sleep(5)
#             ssr1.set_state_off()
#             ssr2.set_state_pulse()
#             time.sleep(5)
#             ssr1.set_state_pulse()
#             ssr2.set_state_on()
#             time.sleep(5)
#         except KeyboardInterrupt:
#             break
        
#     pattern.close(device_data)
#     device.close(device_data)