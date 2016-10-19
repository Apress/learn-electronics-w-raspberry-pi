#!/usr/bin/python3
import time
from gpiozero import Robot
import RPi.GPIO as GPIO


robot = Robot(left=(17, 18), right=(22, 23))

# Ultrasonic range sensor (pins)
pin_trig = 13
pin_echo = 26

## These may need to be adjusted depending upon the size of the robot and the speed of the motors 
# minimum distance before we turn in cm
min_distance = 13
# speed when moving forward (between 0 and 1)
speed_forward = 0.8
# speed when turning (between 0 and 1)
speed_turn = 0.6

# Setup GPIO input/output and disable warnings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings (False)
GPIO.setup(pin_trig, GPIO.OUT)
GPIO.setup(pin_echo, GPIO.IN)

# Set ultrasonic sensor off and wait to settle
GPIO.output(pin_trig, 0)
time.sleep(0.5)

while True:
    # sleep to ensure we don't try to recalc distance before it's settled
    time.sleep(0.5)
    
    
    # Check for distance in front
    # Send 10micro sec pulse 
    GPIO.output(pin_trig, 1)
    time.sleep(0.000001)
    GPIO.output(pin_trig, 0)
    
    # Wait until input goes high - then wait for it to do low
    while (GPIO.input(pin_echo)==0):
        pass
    # Start timer 
    start_time = time.time()
    
    # wait until it goes low again
    while (GPIO.input (pin_echo)==1):
        current_time = time.time()
        # If no response in reasonable time then not received a response (either too close to an object - or too far)
        if ((current_time - start_time)>0.05):
            break
            
    # Calculate response time
    response_time = current_time - start_time;
    
    #distance is time * speed sound (34029cm/s) - divide by 2 for return journey
    distance = response_time * 34029 / 2
    
    # if we are close to a wall then turn right 
    if (distance < min_distance) :
        print ("Too close " + str(distance) + " turning")
        robot.right(speed_turn)
    else :
        robot.forward(speed_forward)

robot.close()
restore_terminal()
GPIO.cleanup()

