
from WF_SDK import device, pattern, error   # import instruments

class PulseGenerator:
    """Diligent Digital Discovery pulse pattern generator"""
    def __init__(self):
        self.device_data = device.open()
        self.running = False
        
    def run(self, dio_out, frequency, duty_cycle):
        """Generate a certain freq PWM signal 
        with certain % duty cycle on a DIO channel.
        Allows user to change pattern on the fly.
        """
        if self.running:
            self.stop()
        pattern.generate(self.device_data, channel=dio_out, 
                         function=pattern.function.pulse, 
                         frequency=frequency, 
                         duty_cycle=duty_cycle)
        self.running = True

    def stop(self):
        """stop the pattern generator"""
        if self.running:
            pattern.close(self.device_data)
            self.running = False

    def __del__(self):
        """close the connection"""
        if self.running:
            self.stop()
        device.close(self.device_data)
