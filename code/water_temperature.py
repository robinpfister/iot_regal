from ds18x20 import DS18X20
import time

addresses = { "Red" : bytearray(b'(\xffd\x1f[\xcd\xa3.'),
             "Orange" : bytearray(b'(\xffd\x1f[\xa0\x1aS'),
             "Yellow" : bytearray(b'(t\xe0V\xb5\x01<\x01'),
             "Black" : bytearray(b'(\x98\x17V\xb5\x01<\xa2'),
             "Blue" : bytearray(b'(F\x19V\xb5\x01<\xd7'),
             "White" : bytearray(b'(G&V\xb5\x01<\x0b'),
             "Green" : bytearray(b'(\xffUV\xb5\x01<\x8e')}

class WaterTemperature():
    def __init__(self, one_wire, addr):
        self.addr = addr
        self.sensor = DS18X20(one_wire)
        
    def get_value(self):
        time.sleep(0.01)
        self.sensor.convert_temp()
        value = self.sensor.read_temp(self.addr)
        return value
        
        