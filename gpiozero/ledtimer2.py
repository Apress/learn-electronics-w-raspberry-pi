#!/usr/bin/python3
# Second LED timer button which accepts optional argument. 
# If a number is provided on the command line then that will be used for the
# delay time. This also uses the keyboard instead of a button press.

from gpiozero import LED
import time
import sys

# Time to keep the light on in seconds
DEFAULTDELAY = 30

# GPIO port numbers for the LED
LED_PIN = 4

if ((len(sys.argv) > 1) and (int(sys.argv[1]) > 0)):
    delay = int(sys.argv[1])
else:
    delay = DEFAULTDELAY

led = LED(LED_PIN)

while True:
	input("Press enter to turn the light on for "+str(delay)+" seconds")
	led.on()
	time.sleep(delay)
	led.off()

