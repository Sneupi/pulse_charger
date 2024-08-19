from WF_SDK import device, static, supplies, error

class DiligentSupply:
    """Tiny power source supplied by Diligent device"""
    def __init__(self, device_data, voltage, current):
        self.device_data = device_data
        self.supplies_data = self._init_supply(device_data, voltage, current)
        self.turn_off()
        
    def _init_supply(self, device_data, voltage, current):
        # start the positive supply
        supplies_data = supplies.data()
        supplies_data.master_state = True
        supplies_data.state = True
        supplies_data.voltage = voltage
        # set maximum current
        if device_data.name == "Digital Discovery" or device_data.name == "Analog Discovery Pro 3X50":
            static.set_current(device_data, current)
        return supplies_data

    def _set_state(self, state):
        if self.supplies_data.master_state != state:
            self.supplies_data.master_state = state
            supplies.switch(self.device_data, self.supplies_data)
            
    def turn_on(self):
        self._set_state(True)
    
    def turn_off(self):
        self._set_state(False)
        
    def close(self):
        """Shut the power supply"""
        # stop the static I/O
        static.close(self.device_data)
        # stop and reset the power supplies
        self._set_state(False)
        supplies.close(self.device_data)
    
    def __del__(self):
        try:
            self.close()
        except Exception as e:
            pass
        
# device_data = device.open()
# supply = DiligentSupply(device_data, 5, 0.1)

# on = False
# try:
#     while True:
#         input()
#         on = not on
#         if on:
#             print("Turning on")
#             supply.turn_on()
#         else:
#             print("Turning off")
#             supply.turn_off()
        
# except KeyboardInterrupt:
#     print("EXITING FROM CTRL+C")

# except error as e:
#     print(e)

# finally:
#     supply.close()
#     device.close(device.data)