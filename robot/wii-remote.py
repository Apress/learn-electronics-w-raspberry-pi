#!/usr/bin/python
import cwiid
import time

delay = 0.2

print ("Press 1 + 2 on the Wii Remote")
time.sleep(1)


wii = cwiid.Wiimote()

print ("Connected\n")
    
# Testing button mode
wii.rpt_mode = cwiid.RPT_BTN


while True :
    
    buttons = wii.state["buttons"]
    
    button_string = ""

    # The vaue of each button is added together so use a bitwise and to test each button
    if (buttons & cwiid.BTN_1):
        button_string += " 1"
    if (buttons & cwiid.BTN_2):
        button_string += " 2"
    if (buttons & cwiid.BTN_A):
        button_string += " A"
    if (buttons & cwiid.BTN_B):
        button_string += " B"
    if (buttons & cwiid.BTN_UP):
        button_string += " up"
    if (buttons & cwiid.BTN_RIGHT):
        button_string += " right"
    if (buttons & cwiid.BTN_DOWN):
        button_string += " down"
    if (buttons & cwiid.BTN_LEFT):
        button_string += " left"
    if (buttons & cwiid.BTN_PLUS):
        button_string += " plus"
    if (buttons & cwiid.BTN_MINUS):
        button_string += " minus"
    if (buttons & cwiid.BTN_HOME):
        button_string += " home"
        
    if (button_string != ""):
        print ("Buttons pressed :" + button_string)
    time.sleep(delay)
