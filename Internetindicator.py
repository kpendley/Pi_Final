#!/bin/python3

from gpiozero import LED, PingServer, Button
from gpiozero.tools import negated
from signal import pause

button = Button(26)
clear = LED(2)
green = LED(3)
yellow = LED(4)
red = LED(17)

while true:
        button.when_pressed()

        print "Connection inquired"

        google = PingServer('google.com')

        google.when_activated = green.on
        google.when_deactivated = green.off
        red.source = negated(green)

pause()
