# Find the Glowstone
from mcpi.minecraft import Minecraft
import mcpi.block as block
from gpiozero import LED
import time, random

mc = Minecraft.create()

RED_LED = 12
GREEN_LED = 16

red_led = LED(RED_LED)
green_led = LED(GREEN_LED)

# min depth and max depth should both be positive (relative to 0)
max_depth = 30
min_depth = 5
max_distance = 100

# Hide the Glowstone
x_pos = random.randrange(0, max_distance * 2)
x_pos = x_pos - max_distance
z_pos = random.randrange(0, max_distance * 2)
z_pos = z_pos - max_distance
y_pos = random.randrange(min_depth, max_depth,1)
y_pos = y_pos * -1
mc.setBlock (x_pos, y_pos, z_pos, block.GLOWSTONE_BLOCK.id)

print ("Glowstone is at "+str(x_pos)+" "+str(y_pos)+" "+str(z_pos))

start_time = time.time()

last_position = mc.player.getTilePos()

while True:
    position_difference = 0
    current_position = mc.player.getTilePos()
    print_string = "Current "+str(current_position.x)+" "+str(current_position.y)+" "+str(current_position.z)
    # Diff in x direction
    old_diff = abs(x_pos - last_position.x)
    new_diff = abs(x_pos - current_position.x)
    position_difference = position_difference + new_diff - old_diff
    print_string = print_string + " X diff:"+str(new_diff-old_diff)
    # Diff in y direction
    old_diff = abs(y_pos - last_position.y)
    new_diff = abs(y_pos - current_position.y)
    position_difference = position_difference + new_diff - old_diff
    print_string = print_string + " Y diff:"+str(new_diff-old_diff)
    # Diff in z direction
    old_diff = abs(z_pos - last_position.z)
    new_diff = abs(z_pos - current_position.z)
    position_difference = position_difference + new_diff - old_diff
    print_string = print_string + " Z diff:"+str(new_diff-old_diff)
    
    if (last_position.x != current_position.x or \
        last_position.y !=  current_position.y or \
        last_position.z != current_position.z):
        print (print_string+" Total:"+str(position_difference))
    
        if (position_difference > 0) :
            red_led.on()
            green_led.off()
        elif (position_difference < 0) :
            red_led.off()
            green_led.on()
        else :
            red_led.on()
            green_led.on()
            
        last_position = current_position
    
    # check to see if the block has been destroyed
    block_id = mc.getBlock(x_pos, y_pos, z_pos)
    if (block_id != block.GLOWSTONE_BLOCK.id): 
        break
    
    time.sleep (0.1)
    
end_time = time.time()
timetaken = int(end_time - start_time)
mc.postToChat("Well done - it took you "+str(timetaken)+" seconds")

