from machine import Pin
from bme680 import BME680_I2C

class BME:
    def __init__(self, i2c, address):
        self.sensor = BME680_I2C(i2c, address)
        

    def get_temp(self):
        # read out temperature from sensor here
        temperature = self.sensor.temperature
        return temperature #in °C
    
    def get_voc_vsc(self):
        # read out voc_vsc value from sensor here
        # assueming it is a combined value --> split if different values
        voc_vsc = self.sensor.gas
        return voc_vsc #in KOhms
    
    def get_humdidity(self):
        # read out humidity from sensor here
        humidity = self.sensor.humidity
        return humidity

    def get_pressure(self):
        # read out pressure from sensor here
        pressure = self.sensor.pressure
        return pressure