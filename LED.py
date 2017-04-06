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

    def transition(self, toRed, toGreen, toBlue, speed):
        rBeg = self.red
        gBeg = self.green
        bBeg = self.blue
        rDiff = abs(rBeg - toRed)/100
        gDiff = abs(gBeg - toGreen)/100
        bDiff = abs(bBeg - toBlue)/100

        print("Increments:\nr:",rDiff,"g:", gDiff,"b", bDiff,"\n")
        step = -1
        while(self.red == rBeg and self.green == gBeg and self.blue == bBeg):
            if step > 0:
                step = 1
            else:
                step = -1

            for i in range(0,100,step):
                red = rBeg + i*rDiff
                green = gBeg + i*gDiff
                blue = bBeg + i*bDiff
                time.sleep(speed/100)
                pi.set_PWM_dutycycle(r, red * self.power)
                pi.set_PWM_dutycycle(g, green * self.power)
                pi.set_PWM_dutycycle(b, blue * self.power)

    def off(self):
        pi.set_PWM_dutycycle(r, 0)
        pi.set_PWM_dutycycle(g, 0)
        pi.set_PWM_dutycycle(b, 0)
