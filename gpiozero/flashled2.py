from gpiozero import LED
import time

LED_PIN = 22

led = LED(LED_PIN)

while True:
	print ("on")
	led.on()
	time.sleep(1)
	print ("off")
	led.off()
	time.sleep(1)

