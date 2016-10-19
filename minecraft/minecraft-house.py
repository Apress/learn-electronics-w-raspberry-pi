# Build a house in Minecraft
import mcpi.minecraft as minecraft
import mcpi.block as block
from mcpi.minecraft import Minecraft
from gpiozero import Button
import time

# Setup various buttons and connect to minecraft
mc = Minecraft.create()

BTN_HOUSE = 18

# House size
house_size_x = 16
house_size_y = 6
house_size_z = 10

# Save position of house here 
# allows us to go to it later
# if not defined then leave at 0,0,0
# vec3 allows us to create a position vector
house_position = minecraft.Vec3(0,0,0)

# Time to wait before moves
DELAY = 1

# Main loop to monitor buttons
def main():
    btn_house = Button(BTN_HOUSE)
    
    while True:
        if (btn_house.is_pressed) :
            # Set position to current location
            # This will be the centre of the house
            house_position = mc.player.getTilePos()
            build_house(house_position, house_size_x, house_size_y, house_size_z)
            # Delay before next instruction
            time.sleep(DELAY)
    time.sleep (0.2)


def build_house (house_position, house_size_x, house_size_y, house_size_z):
    # clear blocks where the house is to be built
    mc.setBlocks (                                 \
        house_position.x - (house_size_x / 2),     \
        house_position.y,                          \
        house_position.z - (house_size_z / 2),     \
        house_position.x + (house_size_x / 2),     \
        house_position.y + house_size_y,           \
        house_position.z + (house_size_z / 2),     \
        block.AIR.id)
    # Build floor 
    mc.setBlocks (                                 \
        house_position.x - (house_size_x / 2),     \
        house_position.y - 1,                      \
        house_position.z - (house_size_z / 2),     \
        house_position.x + (house_size_x / 2),     \
        house_position.y - 1,                      \
        house_position.z + (house_size_z / 2),     \
        block.COBBLESTONE.id) 
    # build front wall - north wall
    mc.setBlocks (                                 \
        house_position.x - (house_size_x / 2),     \
        house_position.y,                          \
        house_position.z - (house_size_z / 2),     \
        house_position.x + (house_size_x / 2),     \
        house_position.y + house_size_y,           \
        house_position.z - (house_size_z / 2),     \
        block.BRICK_BLOCK.id)
    # build rear wall - south wall
    mc.setBlocks (                                 \
        house_position.x - (house_size_x / 2),     \
        house_position.y,                          \
        house_position.z + (house_size_z / 2),     \
        house_position.x + (house_size_x / 2),     \
        house_position.y + house_size_y,           \
        house_position.z + (house_size_z / 2),     \
        block.BRICK_BLOCK.id)
    # build side wall - east wall
    mc.setBlocks (                                 \
        house_position.x + (house_size_x / 2),     \
        house_position.y,                          \
        house_position.z - (house_size_z / 2),     \
        house_position.x + (house_size_x / 2),     \
        house_position.y + house_size_y,           \
        house_position.z + (house_size_z / 2),     \
        block.BRICK_BLOCK.id)
    # build side wall - west wall
    mc.setBlocks (                                 \
        house_position.x - (house_size_x / 2),     \
        house_position.y,                          \
        house_position.z - (house_size_z / 2),     \
        house_position.x - (house_size_x / 2),     \
        house_position.y + house_size_y,           \
        house_position.z + (house_size_z / 2),     \
        block.BRICK_BLOCK.id)
    # Build roof
    mc.setBlocks (                                 \
        house_position.x - (house_size_x / 2),     \
        house_position.y + house_size_y + 1,       \
        house_position.z - (house_size_z / 2),     \
        house_position.x + (house_size_x / 2),     \
        house_position.y + house_size_y + 1,       \
        house_position.z + (house_size_z / 2),     \
        block.WOOD.id)

    # Frame of house now built - add doors and windows
    # Make doorway out of air block
    mc.setBlocks (                                 \
        house_position.x,                          \
        house_position.y,                          \
        house_position.z - (house_size_z / 2),     \
        house_position.x + 1,                      \
        house_position.y + 2,                      \
        house_position.z - (house_size_z / 2),     \
        block.AIR.id)
    
    # Add 2 windows
    mc.setBlocks (                                 \
        house_position.x + (house_size_x / 4),     \
        house_position.y + (house_size_y / 2),     \
        house_position.z - (house_size_z / 2),     \
        house_position.x + (house_size_x / 4) + 2, \
        house_position.y + (house_size_y / 2) + 2, \
        house_position.z - (house_size_z / 2),     \
        block.GLASS.id)

    mc.setBlocks (                                 \
        house_position.x - (house_size_x / 4),     \
        house_position.y + (house_size_y / 2),     \
        house_position.z - (house_size_z / 2),     \
        house_position.x - (house_size_x / 4) - 2, \
        house_position.y + (house_size_y / 2) + 2, \
        house_position.z - (house_size_z / 2),     \
        block.GLASS.id)


#Run the main function when this program is run
if __name__ == "__main__":
    main()


