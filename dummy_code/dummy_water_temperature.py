class WaterTemperature:
    def __init__(self, one_wire, address):
        """
        @one_wire: one wire element
        @address: address of sensor
        """
        self.one_wire = one_wire
        self.address = address
        # add one wire initialization here
        
    def get_value(self):
        """returns temp in °C"""
        return 23.7