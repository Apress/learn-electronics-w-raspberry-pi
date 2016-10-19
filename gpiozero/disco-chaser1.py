from gpiozero import LED
import time

# GPIO port numbers for the light
#9 = gnd, 7 = GPIO 4, 11 = GPIO 17, 16 = GPIO 23, 18 = GPIO 24
LIGHTGPIO = [4, 17, 23, 24]
# Time between each step in the sequence in seconds
DELAY = 1

lights = [LED(LIGHTGPIO[0]), LED(LIGHTGPIO[1]), LED(LIGHTGPIO[2]), LED(LIGHTGPIO[3])]

# Track our position in the sequence
seq_number = 0

while True :
    if (seq_number > 3):
        seq_number = 0
    for x in range (4):
        lights[x].off()
    lights[seq_number].on()
    seq_number = seq_number + 1
    time.sleep(DELAY)

