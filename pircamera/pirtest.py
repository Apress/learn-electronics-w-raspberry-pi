from gpiozero import MotionSensor
import time

# PIR sensor on GPIO pin 4
PIR_SENSOR_PIN = 4
# Minimum time between captures
DELAY = 5

pir = MotionSensor(PIR_SENSOR_PIN)

while True:
    pir.wait_for_motion()
    print ("Motion detected")
    time.sleep(DELAY)
