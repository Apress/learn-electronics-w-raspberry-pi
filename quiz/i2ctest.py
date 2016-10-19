from I2CDisplay import *
import time

# Initialise display
lcd_init()

# Send some test
lcd_string("Learn Electronics",LCD_LINE_1)
lcd_string("with Raspberry Pi",LCD_LINE_2)
lcd_string("by",LCD_LINE_3)
lcd_string("Stewart Watkiss",LCD_LINE_4)

time.sleep(20)
lcd_clear()

