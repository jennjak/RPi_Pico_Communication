#toggles the led and send print string to PC

import time
from machine import Pin
from picozero import pico_led

while True:
    pico_led.on()
    time.sleep(0.5)   
    print("test communication UART" + "\n")
    pico_led.off()
    time.sleep(0.5)
    print("test2 communication UART" + "\n")
