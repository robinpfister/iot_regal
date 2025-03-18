from tsl2561 import TSL2561

class Luminosity:
    def __init__(self, i2c, address):
        # Sensor setup using the Adafruit TSL2561 library.
        self.sensor = TSL2561(i2c, address)

    def get_value(self):
        # If the sensor is overloaded, a ValueError is thrown.
        # Catch this to avoid a crash.
        try:
            value = self.sensor.read()
        except ValueError:
            value = -1.0
        
        return value