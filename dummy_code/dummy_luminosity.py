class Luminosity:
    def __init__(self, i2c, address):
        self.i2c = i2c # i2c instantiation is done by parrent
        self.address = address

    def get_value(self):
        return 300.34 #in Lux
