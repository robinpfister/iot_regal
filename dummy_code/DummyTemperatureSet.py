class DummyTemperatureSet:
    def __init__(self, pin, addresses):
        """
        @pin: one wire pin
        @addresses: dict = {
         "Left": adr
         "Middle": adr
         "Right": adr
        }
        """
        self.pin = pin
        # add one wire initialization here
        
    def getValue():
        """returns dict in °C"""
        values = {
            "Left": 23.3,
            "Middle": 27.5,
            "Right": 10.8}
        return values