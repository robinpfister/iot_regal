class Fan:
    def __init__(self, pwm_pin):
        self.pwm_pin = pwm_pin
        # initialize PWM here
        
    def set_value(self, duty_cycle):
        """@duty_cylce: 1byte value"""
        print("Message on Fan topic received")
        # set pwm to drive fan