#!/bin/python

from gpiozero import LED
from icmplib  import ping
from gpiozero import Button
from gpiozero import PWMLED
from time import sleep

button = Button(26)

clear = LED(2)
green = LED(3)
yellow = PWMLED(4)
red = LED(27)


# host = ping('8.8.8.8')

while True:
        clear.on()
        green.off()
        yellow.on()
        button.wait_for_press()
        print("Connection inquired")
        host = ping('8.8.8.8')
        print (host)
        print (host.packets_received)
        if host.packets_received >3:
                yellow.off()
                green.on()
                sleep(5)
        else:
                yellow.off()
                red.on()
                sleep(5)
        if host.packet_loss >1:
                yellow.value = 1
                sleep(0.2)
                yellow.value = 0
                sleep(0.2)
                yellow.value = 1
                sleep(0.2)
                yellow.value = 0
