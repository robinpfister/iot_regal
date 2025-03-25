class BMETemp:
    """wrapper around bme"""
    def __init__(self, bme):
        self.bme = bme

    def get_value(self):
        return self.bme.get_temp()
    