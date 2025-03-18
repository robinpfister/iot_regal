from machine import Pin

class FlowSensor():
    
    def __init__(self, pin)
        self.pin = Pin(pin, mode=Pin.IN)


    def get_value(self):
        return self.pin.value