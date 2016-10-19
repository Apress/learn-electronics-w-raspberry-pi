import lirc
from gpiozero import LED

# GPIO port number for the LED
LED_PIN = 22

sockid = lirc.init("testlirc")
led = LED(LED_PIN)


while True:
    code = lirc.nextcode()
    if (len(code)>0):
        if (code[0] == "Power"):
            led.toggle()


