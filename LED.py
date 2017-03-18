# import RPi.GPIO as GPIO
# import time
import pigpio

class LED():
    red = 0
    green = 0
    blue = 0
    power = 1

    def __init__(self, red: int, green: int, blue: int, power: int):
        self.red = red
        self.green = green
        self.blue = blue
        self.power = power

    def update(self, red, green, blue, power):
        self.red = red
        self.green = green
        self.blue = blue
        self.power = power

# pi = pigpio.pi()
# pi.set_PWM_dutycycle(PIN, BRIGHTNESS)
# pi.stop()