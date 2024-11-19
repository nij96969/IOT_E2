from gpiozero import LED
from time import sleep

led = LED(4)

try:
    while True:
        led.on()
        sleep(1)
        print("1")
        led.off()
        sleep(1)
        print("2")
except KeyboardInterrupt:
    pass
