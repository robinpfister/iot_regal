from machine import I2C, Pin
from onewire import OneWire
from ds18x20 import DS18X20

ow1 = OneWire(Pin(1))

s = DS18X20(ow1)

print(s.scan())

