import machine

class Illumination():
    
    pin
    
    __init__(self, illumination_pin):
        pin = machine.Pin(illumination_pin, machine.Pin.OUT)
        
    def set_value(set_enable):
        """@set_enable: 0 or 1"""
        pin.value(set_enable)