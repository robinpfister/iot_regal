class Illumination:
    def __init__(self, light_pin):
        self.light_pin = light_pin
        # initialize PWM here
        
    def set_value(self, turn_on):
        """@turn_on: bool to set light"""
        print("Message on Fan topic received")
        # set digital pin accordingly