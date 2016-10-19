import picamera
import time

camera = picamera.PiCamera()

timestring = time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime())

camera.capture('/home/pi/photo_'+timestring+'.jpg')
camera.close()
