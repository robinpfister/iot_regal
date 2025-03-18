import machine

class Fan():
    
    pin
    pwm
    
    __init__(self, pwm_pin):
        pin = machine.Pin(pwm_pin)
        pwm = machine.PWM(pin)
        pwm.freq(1000)
        
    def set_value(duty_cycle):
        """@duty_cylce: 1byte value"""
        pwm.duty(duty_cycle*4)