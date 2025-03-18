class BME():
    def __init__(self, i2c, address):
        self.i2c = i2c # i2c instantiation is done by parrent
        self.address = address
        
    def get_temp():
        # read out temperature from sensor here
        return 23.3 #°C
    
    def get_voc_vsc():
        # read out voc_vsc value from sensor here
        # assueming it is a combined value --> split if different values
        return 124
    def get_pressure():
        # read pressure
        return 1096 #°mBar