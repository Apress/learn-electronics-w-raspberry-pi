#!/usr/bin/python3
import picamera, lirc, time, os.path

# Minimum time between captures
DELAY = 0.5

# Directory for photos
photodir = '/home/pi/film';

# Create lirc socket
sockid = lirc.init("ircamera")

# Create camera object
camera = picamera.PiCamera(resolution=(720,576))
camera.hflip=True
camera.vflip=True

imagenum = 1

while True:
    image_string = u'%04d' % imagenum
    filename = photodir+'/photo_'+image_string+'.jpg'
    # Loop to ensure that filename is unique
    while os.path.isfile(filename):
        imagenum = imagenum + 1
        image_string = u'%04d' % imagenum
        filename = photodir+'/photo_'+image_string+'.jpg'
    
    camera.start_preview()
    code = lirc.nextcode()
    if (len(code)>0):
        if (code[0] == "Enter"):
            print ("Taking photo " +filename)
            camera.capture(filename)
            time.sleep(DELAY)
            imagenum = imagenum + 1
        elif (code[0] == "Power"):
            break

            
camera.close()

