import pigpio

pi = pigpio.pi()
r = 17
g = 22
b = 24

class LED():
    red = 0
    green = 0
    blue = 0
    power = 1

    def __init__(self, red: int, green: int, blue: int, power: float):
        self.red = red
        self.green = green
        self.blue = blue
        self.power = power

    def update(self, red, green, blue, power):
        self.red = red
        self.green = green
        self.blue = blue
        self.power = power

    def gpio(self):
        pi.set_PWM_dutycycle(r, self.red*self.power)
        pi.set_PWM_dutycycle(g, self.green*self.power)
        pi.set_PWM_dutycycle(b, self.blue*self.power)

    def off(self):
        pi.set_PWM_dutycycle(r,0)
        pi.set_PWM_dutycycle(g,0)
        pi.set_PWM_dutycycle(b,0)

# pi.stop()
