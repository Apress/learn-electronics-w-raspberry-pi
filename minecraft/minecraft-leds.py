# Scan underground blocks and light LEDs to show status
from mcpi.minecraft import Minecraft
import mcpi.block as block
from gpiozero import Button, LED
import time

# Connect to minecraft
mc = Minecraft.create()

DELAY = 0.2

# Number of blocks to scan for
DEPTH = 50

COAL_RED = 12
COAL_GREEN = 16
IRON_RED = 20
IRON_GREEN = 21
DIAMOND_RED = 26
DIAMOND_GREEN = 19
LAVA_RED = 13

coal_red = LED(COAL_RED)
coal_green = LED(COAL_GREEN)
iron_red = LED(IRON_RED)
iron_green = LED(IRON_GREEN)
diamond_red = LED(DIAMOND_RED)
diamond_green = LED(DIAMOND_GREEN)
lava_red = LED(LAVA_RED)

# track current status of lava - so we can make it flash
lava_flash = 0

while True:
    # variables to identify the number of blocks we have found
    coal_found = 0
    iron_found = 0
    diamond_found = 0
    lava_found = 0

    # Get position
    position = mc.player.getTilePos()

    for i in range (0, DEPTH):
        # Get ID of next block
        block_id = mc.getBlock(position.x, position.y - i, position.z)
        if (block_id == block.COAL_ORE.id):
            coal_found = coal_found + 1
        elif (block_id == block.IRON_ORE.id):
            iron_found = iron_found + 1
        elif (block_id == block.DIAMOND_ORE.id):
            diamond_found = diamond_found + 1
        elif (block_id == block.LAVA.id):
            lava_found = lava_found + 1

    print ("Checking position "+str(position.x)+" "+str(position.y)+" "+str(position.z)+" Coal "+str(coal_found)+ " Iron "+str(iron_found)+" Diamond "+str(diamond_found)+" Lava "+str(lava_found))
    # Update LEDs based on what found - 0 = red, 1 = orange, s+ = green
    if (coal_found < 1):
        coal_red.on()
        coal_green.off()
    elif (coal_found < 2):
        coal_red.on()
        coal_green.on()
    else: # 2 or more
        coal_red.off()
        coal_green.on()
    
    if (iron_found < 1):
        iron_red.on()
        iron_green.off()
    elif (iron_found < 2):
        iron_red.on()
        iron_green.on()
    else: # 2 or more
        iron_red.off()
        iron_green.on()


    if (diamond_found < 1):
        diamond_red.on()
        diamond_green.off()
    elif (diamond_found < 2):
        diamond_red.on()
        diamond_green.on()
    else: # 2 or more
        diamond_red.off()
        diamond_green.on()

    # different with lava - instead flash LED
    # toggle status on each iteration around the loop
    if (lava_found > 0 or position.y < -50) :
        lava_flash = 1 - lava_flash
        if (lava_flash == 1) :
            lava_red.on()
        else :
            lava_red.off()
    else:
        lava_red.off()



