from gpiozero import LED, Button
import time

# GPIO port numbers for the LED and Button
LED_PIN = 22
BUTTON_PIN = 10
# Time to keep the light on in seconds
DELAY = 30

led = LED(LED_PIN)
button = Button(BUTTON_PIN)

while True:
	button.wait_for_press()
	led.on()
	time.sleep(DELAY)
	led.off()

