# Scatter some diamond ore in random positions underground
from mcpi.minecraft import Minecraft
import mcpi.block as block
import random

mc = Minecraft.create()

# We may not end up with quite this many if we get any 
# duplicate positions
num_diamonds = 50

# min depth and max depth should both be positive (relative to 0)
max_depth = 30
min_depth = 5
max_distance = 100

for i in range (0, num_diamonds):
    x_pos = random.randrange(0, max_distance * 2)
    x_pos = x_pos - max_distance
    z_pos = random.randrange(0, max_distance * 2)
    z_pos = z_pos - max_distance
    y_pos = random.randrange(min_depth, max_depth,1)
    y_pos = y_pos * -1
    
    # set the appropriate block to a diamond
    print ("Setting diamond at "+str(x_pos)+" "+str(y_pos)+" "+str(z_pos))
    mc.setBlock (x_pos, y_pos, z_pos, block.DIAMOND_ORE.id)
