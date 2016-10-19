from gpiozero import MotionSensor
import picamera
import time

# PIR sensor on GPIO pin 4
PIR_SENSOR_PIN = 4
# Minimum time between captures
DELAY = 5

# Create pir and camera objects
pir = MotionSensor(PIR_SENSOR_PIN)
camera = picamera.PiCamera()

while True:
    pir.wait_for_motion()
    timestring = time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime())
    print ("Taking photo " +timestring)
    camera.capture('/home/pi/photo_'+timestring+'.jpg')
    time.sleep(DELAY)
