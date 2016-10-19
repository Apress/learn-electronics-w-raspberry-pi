import spidev
import time

# Sensor Port - where analog device is connected to
sensorChannel = 0

spi = spidev.SpiDev()
# Open connection to SPI device: Bus 0, Device 0
spi.open(0,0)

# Read using SPI - A to D convertor
# Has 0 to 7 inputs
# Returns integer of value read 0 to 1023
# or returns -1 on error
def readAnalog(input):
    if (input < 0 or input > 7):
        return -1
    req = 8+input
    # shift to higher bits
    req = req << 4
    # 1 and 0 are start and stop values in tuple
    resp = spi.xfer2([1,req,0])
    # resp is split across two entries [1] and [2]
    # shift and merge these together
    high = resp[1]&3
    low = resp[2]
    return ((high<<8) + low)



while True:
    analogValue = readAnalog(sensorChannel)
    print ("Value : " + str(analogValue))
    time.sleep(1)

