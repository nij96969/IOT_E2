from gpiozero import LED, Button
from time import sleep

# Define GPIO pins for the LED and switch
LED_PIN = 4      # GPIO pin connected to the LED
BUTTON_PIN = 17  # GPIO pin connected to the switch

# Create LED and Button objects
led = LED(LED_PIN)
button = Button(BUTTON_PIN)

print("Press and hold the button to turn on the LED. Release to turn it off.")

try:
    while True:
        if button.is_pressed:  # Check if the button is pressed
            led.on()  # Turn on the LED
        else:
            led.off()  # Turn off the LED
        sleep(0.1)  # Short delay to reduce CPU usage
except KeyboardInterrupt:
    print("\nExiting program.")
finally:
    led.off()  # Ensure the LED is off on exit
