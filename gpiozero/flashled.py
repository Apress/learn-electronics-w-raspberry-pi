from gpiozero import LED
import time

LEP_PIN = 17

led = LED(LED_PIN)

print ("off")
led.off()
time.sleep(1)
print ("on")
led.on()
time.sleep(1)
print ("off")
led.off()
time.sleep(1)
print ("on")
led.on()
time.sleep(1)
