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
    fading = False

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

    def fade(self, toRed, toGreen, toBlue, speed=65):
        self.fading = True
        rBeg = self.red
        gBeg = self.green
        bBeg = self.blue

        rDiff = (toRed - self.red) / 100
        gDiff = (toGreen - self.green) / 100
        bDiff = (toBlue - self.blue) / 100
        print("Increments:\nr:{0}, g:{1}, b:{2}".format(rDiff, gDiff, bDiff))
        step = -1

        while self.fading:
            if step > 0:
                beg = 100
                end = 0
                step = -1
            else:
                beg = 0
                end = 100
                step = 1
            for i in range(beg, end, step):
                if not self.fading:
                    break
                red = rBeg + i * rDiff
                green = gBeg + i * gDiff
                blue = bBeg + i * bDiff
                pi.set_PWM_dutycycle(r, red * self.power)
                pi.set_PWM_dutycycle(g, green * self.power)
                pi.set_PWM_dutycycle(b, blue * self.power)
                time.sleep(speed / 1000)

        print("EXITING FADE")

    def off(self):
        pi.set_PWM_dutycycle(r, 0)
        pi.set_PWM_dutycycle(g, 0)
        pi.set_PWM_dutycycle(b, 0)
