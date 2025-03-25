from water_temperature import WaterTemperature, addresses
import time
from luminosity import Luminosity
from machine import I2C, Pin
from onewire import OneWire
from flowsensor import Flowsensor
from bme import BME

ow1 = OneWire(Pin(1))
ow2 = OneWire(Pin(2))

i2c0 = I2C(0, sda = Pin(5), scl = Pin(4))
i2c1 = I2C(1, sda = Pin(7), scl = Pin(6))

t_red = WaterTemperature(ow1, addresses["Red"])
t_orange = WaterTemperature(ow1, addresses["Orange"])
t_yellow = WaterTemperature(ow1, addresses["Yellow"])
t_black = WaterTemperature(ow1, addresses["Black"])
t_blue = WaterTemperature(ow2, addresses["Blue"])
t_green = WaterTemperature(ow2, addresses["Green"])
t_white = WaterTemperature(ow2, addresses["White"])

l1 = Luminosity(i2c0, 0x39)
l2 = Luminosity(i2c0, 0x29)
l3 = Luminosity(i2c1, 0x39)
l4 = Luminosity(i2c1, 0x29)


f1 = Flowsensor(40)
f2 = Flowsensor(41)
f3 = Flowsensor(42)


b1 = BME(i2c0, 0x77)
b2 = BME(i2c0, 0x76)
b3 = BME(i2c1, 0x77)
b4 = BME(i2c1, 0x76)


while True:
    print(f't_red: {t_red.get_value()}')
    print(f't_orange: {t_orange.get_value()}')
    print(f't_yellow: {t_yellow.get_value()}')
    print(f't_black: {t_black.get_value()}')
    print(f't_blue: {t_blue.get_value()}')
    print(f't_green: {t_green.get_value()}')
    print(f't_white: {t_white.get_value()}')
    print(f'l1: {l1.get_value()}')
    print(f'l2: {l2.get_value()}')
    print(f'l3: {l4.get_value()}')
    print(f'l4: {l3.get_value()}')
    print(f'f1: {f1.get_value()}')
    print(f'f2: {f2.get_value()}')
    print(f'f3: {f3.get_value()}')
    print(f'b1 temp: {b1.get_temp()}')
    print(f'b2 temp: {b2.get_temp()}')
    print(f'b3 temp: {b3.get_temp()}')
    print(f'b4 temp: {b4.get_temp()}')
    print(f'b1 voc/vsc: {b1.get_voc_vsc()}')
    print(f'b2 voc/vsc: {b2.get_voc_vsc()}')
    print(f'b3 voc/vsc: {b3.get_voc_vsc()}')
    print(f'b4 voc/vsc: {b4.get_voc_vsc()}')
    print(f'b1 humidity: {b1.get_humdidity()}')
    print(f'b2 humidity: {b2.get_humdidity()}')
    print(f'b3 humidity: {b3.get_humdidity()}')
    print(f'b4 humidity: {b4.get_humdidity()}')
    print(f'b1 pressure: {b1.get_pressure()}')
    print(f'b2 pressure: {b2.get_pressure()}')
    print(f'b3 pressure: {b3.get_pressure()}')
    print(f'b4 pressure: {b4.get_pressure()}')
    print()
    time.sleep(2)