#!/usr/bin/python3
import sys, tty, termios
import picamera, time
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

# get a character from the command line
def getch() :
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


# list to convert key presses into motor on/off values to correspond with the direction
# direction based on number keypad
# 8 = fwd, 4 = left, 5 = stop, 6 = right, 2 = rev
# the key for the list is the character 
direction = {
    # number keys
    '2' : "backward",
    '4' : "left",
    '5' : "stop",
    '6' : "right",
    '8' : "forward"
}

current_direction = "stop"
# speed is as a percentage (ie. 100 = top speed)
# start speed is 50% which is fairly slow on a flat surface
speed = 50

print ("Robot control - use number keys to control direction")
print ("Speed " + str(speed) +"% - use +/- to change speed") 

while True:
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

    # Get next key pressed      
    ch = getch()

    # q = quit
    if (ch == 'q') :
        break
    elif (ch == '+') :
        speed += 10
        if speed > 100 :
            speed = 100
        print ("Speed : "+str(speed))
    elif (ch == '-' ) :
        speed -= 10
        if speed < 0 :
            speed = 0
        print ("Speed : "+str(speed))
    elif (ch in direction.keys()) :
        current_direction = direction[ch]
        print ("Direction "+current_direction)
    elif (ch == '0' and camera_enable == True) :
        timestring = time.strftime("%Y-%m-%dT%H.%M,%S", time.gmtime())
        print ("Taking photo " +timestring)
        camera.capture(photo_dir+'/photo_'+timestring+'.jpg')
robot.close()

