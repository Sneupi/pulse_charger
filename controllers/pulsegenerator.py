"""Controller related to the pulse generator used in the pulse charging system"""

from WF_SDK import device, pattern, error   # using the Digilent WaveForms SDK

class PulseGenerator:
    """Pulse pattern generator"""
    def __init__(self, device_data, pin):
        """
        Args:
            device_data (Any): Diligent Digital Discovery device data
            pin (int): Hardware pin number
        """
        self.pin = pin
        self.device_data = device_data
        self.running = False
        
    def run(self, frequency, duty_cycle):
        """Generate a certain freq PWM signal 
        with certain % duty cycle on a DIO channel.
        Allows user to change pattern on the fly.
        """
        pattern.generate(self.device_data, channel=self.pin, 
                         function=pattern.function.pulse, 
                         frequency=frequency, 
                         duty_cycle=duty_cycle)
        self.running = True

    def stop(self):
        """stop the pattern generator"""
        if self.running:
            # hacky, as to not close other pattern channels
            self.run(1, 0)  
            self.running = False
