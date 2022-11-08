#!/bin/python

from gpiozero import LED
from gpiozero import PingServer
from gpiozero import Button
from gpiozero import PWMLED
from gpiozero.tools import negated
from time import sleep

button = Button(26)

clear = LED(2)
green = LED(3)
yellow = PWMLED(4)
red = LED(17)


while True:
        clear.value = 1 # full brightness

        yellow.value = 0 # off
        sleep(.2)
        yellow.value = 0.5 # half brightness
        sleep(.2)
        yellow.value = 1 # full brightness

        button.wait_for_press()
        yellow.value = 0 # off
        print("Connection inquired")

        google = PingServer('google.com')

        google.when_activated = green.on
        google.when_deactivated = green.off
        red.source = negated(green)
