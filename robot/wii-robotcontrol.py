#!/usr/bin/python
import sys, tty, termios
import picamera, time
import cwiid
from gpiozero import Robot

robot = Robot(left=(17, 18), right=(22, 23))
camera_enable = False
try:
    camera = picamera.PiCamera()
    camera.hflip=True
    camera.vflip=True
    camera_enable=True
except:
    print ("Camera not found - disabled");

photo_dir = "/home/pi/photos"

# delay between button presses
delay = 0.2

current_direction = "stop"
# speed is as a percentage (ie. 100 = top speed)
# start speed is 50% which is fairly slow on a flat surface
speed = 100

print ("Press 1 + 2 on the Wii Remote")
time.sleep(1)

# Keep trying to connect to the remote
while True:
    try:
        wii=cwiid.Wiimote()
        break
    except RuntimeError:
        print ("Unable to connect to remote - trying again")
        print ("Press 1 + 2 on the Wii Remote")

print ("Robot control - use arrow buttons to control direction")
print ("Speed " + str(speed) +"% - use +/- to change speed") 

wii.rumble = 1
time.sleep(0.5)
wii.rumble = 0

wii.rpt_mode = cwiid.RPT_BTN

while True:
    last_direction = current_direction
    # Convert speed from percentage to float (0 to 1)
    float_speed = speed / 100
    if (current_direction == "forward") :
        robot.forward(float_speed)
    # rev
    elif (current_direction == "backward") :
        robot.backward(float_speed)
    elif (current_direction == "left") :
        robot.left(float_speed)
    elif (current_direction == "right") :
        robot.right(float_speed)
    # stop
    else :
        robot.stop()

    time.sleep(delay)

    # Get next key pressed      
    buttons = wii.state["buttons"]
    
    # set button to stop so that if no buttons pressed we stop
    current_direction = "stop"

    # + and - = quit
    if ((buttons & cwiid.BTN_PLUS) and (buttons & cwiid.BTN_MINUS)) :
        break
    if (buttons & cwiid.BTN_PLUS):
        speed += 10
        if speed > 100 :
            speed = 100
        print ("Speed : "+str(speed))
    if (buttons & cwiid.BTN_MINUS):
        speed -= 10
        if speed < 0 :
            speed = 0
        print ("Speed : "+str(speed))
    if (buttons & cwiid.BTN_UP):
        current_direction = "forward"
    if (buttons & cwiid.BTN_DOWN):
        current_direction = "backward"
    if (buttons & cwiid.BTN_LEFT):
        current_direction = "left"
    if (buttons & cwiid.BTN_RIGHT):
        current_direction = "right"
    if (buttons & cwiid.BTN_A and camera_enable == True):
        timestring = time.strftime("%Y-%m-%dT%H.%M.%S", time.gmtime())
        print ("Taking photo " +timestring)
        camera.capture(photo_dir+'/photo_'+timestring+'.jpg')
    # Only print direction if it's changed from previous
    if (current_direction != last_direction) :
        print ("Direction "+current_direction)
        
robot.close()

