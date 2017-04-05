import pigpio
import time

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
        pi.set_PWM_dutycycle(r, self.red * self.power)
        pi.set_PWM_dutycycle(g, self.green * self.power)
        pi.set_PWM_dutycycle(b, self.blue * self.power)

    def transition(self, toRed, toGreen, toBlue, toPower):
        rDiff = abs(self.red - toRed)/100
        gDiff = abs(self.green - toGreen)/100
        bDiff = abs(self.blue - toBlue)/100
        pDiff = abs(self.power - toPower)/100
        for i in range(100):
            time.sleep(.05)
            pi.set_PWM_dutycycle(r, (self.red + (rDiff*i)) * (pDiff*i))
            pi.set_PWM_dutycycle(g, (self.green + (gDiff*i)) * (pDiff*i))
            pi.set_PWM_dutycycle(b, (self.blue + (bDiff*i)) * (pDiff*i))

    def off(self):
        pi.set_PWM_dutycycle(r, 0)
        pi.set_PWM_dutycycle(g, 0)
        pi.set_PWM_dutycycle(b, 0)

# pi.stop()
