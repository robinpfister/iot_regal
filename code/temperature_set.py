from ds18x20 import DS18X20
from machine import Pin
from onewire import OneWire

# addresses = { "Red" : bytearray(b'(\xffd\x1f[\xcd\xa3.'),
#             "Orange" : bytearray(b'(\xffd\x1f[\xa0\x1aS'),
#             "Yellow" : bytearray(b"(\xd37\x1c\x91!\x06'"),
#             "Blue" : bytearray(b'(F\x19V\xb5\x01<\xd7'),
#             "White" : bytearray(b'(G&V\xb5\x01<\x0b'),
#             "Green" : bytearray(b'(\xffUV\xb5\x01<\x8e')}

adresses_top = {"Left" : bytearray(b'(\xffd\x1f[\xcd\xa3.'),
                "Middle" : bytearray(b'(\xffd\x1f[\xa0\x1aS'),
                "Right" : bytearray(b"(\xd37\x1c\x91!\x06'")}

adresses_box = {"Left" : bytearray(b'(F\x19V\xb5\x01<\xd7'),
                "Middle" : bytearray(b'(G&V\xb5\x01<\x0b'),
                "Right" : bytearray(b'(\xffUV\xb5\x01<\x8e')}

class TemperatureSet():
    def __init__(self, bus_pin, addr):
        self.left_addr = addr["Left"]
        self.middle_addr = addr["Middle"]
        self.right_addr = addr["Right"]
        self.pin = Pin(bus_pin, mode=Pin.IN)
        self.sensor = DS18X20(OneWire(self.pin))
        
    def get_value(self):
        self.sensor.convert_temp()
        left_value = self.sensor.read_temp(self.left_addr)
        middle_value = self.sensor.read_temp(self.middle_addr)
        right_value = self.sensor.read_temp(self.right_addr)
        return {"Left" : left_value,
                "Middle" : middle_value,
                "Right" : right_value}
        
        