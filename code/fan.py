import machine

class Fan():

    def __init__(self, pwm_pin):
        self.pin = machine.Pin(pwm_pin)
        self.pwm = machine.PWM(self.pin)
        self.pwm.freq(25000)
        
    def set_value(self, duty_cycle):
        """@duty_cylce: 1byte value"""
        self.pwm.duty(duty_cycle*4)
        
# fan = Fan(20)
# fan.set_value(255)
# 
# while True:
#     print(fan.pwm)
#     pass