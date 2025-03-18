import machine

class Illumination():
    
    def __init__(self, illumination_pin):
        self.pin = machine.Pin(illumination_pin, machine.Pin.OUT)
        
    def set_value(set_enable):
        """@set_enable: 0 or 1"""
        self.pin.value(set_enable)