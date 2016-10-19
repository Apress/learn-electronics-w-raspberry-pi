from gpiozero import LED
import time

# GPIO port numbers for the light
#9 = gnd, 7 = GPIO 4, 11 = GPIO 17, 16 = GPIO 23, 18 = GPIO 24
LIGHTGPIO = [4, 17, 23, 24]
# Time between each step in the sequence in seconds
DELAY = 1

lights = [LED(LIGHTGPIO[0]), LED(LIGHTGPIO[1]), LED(LIGHTGPIO[2]), LED(LIGHTGPIO[3])]


def allOn():
    for x in range (4):
        lights[x].on()

def allOff():
    for x in range (4):
        lights[x].off()

def sequence():
    for x in range (4):
        for y in range (4):
            lights[y].off()
        lights[x].on()
        time.sleep(DELAY)


def repeatSequence(numsequences):
    for x in range (numsequences):
        sequence()

# Main code starts here
allOff()
time.sleep(DELAY)
allOn()
time.sleep(DELAY)
sequence()
time.sleep(DELAY)
repeatSequence(6)

