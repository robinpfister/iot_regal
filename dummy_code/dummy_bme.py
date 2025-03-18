class BME:
    def __init__(self, i2c, address):
        self.i2c = i2c # i2c instantiation is done by parrent
        self.address = address
        
    def get_temp(self):
        # read out temperature from sensor here
        return 23.3 #°C
    
    def get_voc_vsc(self):
        # read out voc_vsc value from sensor here
        # assueming it is a combined value --> split if different values
        return 124 #what is the unit?
    
    def get_humdidity(self):
        return 30 #in %

    def get_pressure(self):
        # read pressure
        return 1096 #°mBar