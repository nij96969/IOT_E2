import RPi.GPIO as GPIO
import time

# Use the BCM pin numbering
GPIO.setmode(GPIO.BCM)

# Set up GPIO pin 4 as an output
LED_PIN = 4
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        # Turn the LED on
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(1)  # Wait for 1 second

        # Turn the LED off
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(1)  # Wait for 1 second

except KeyboardInterrupt:
    # Cleanup GPIO settings before exiting
    GPIO.cleanup()
