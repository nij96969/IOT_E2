import time
import board
import adafruit_dht
import requests
import json
import RPi.GPIO as GPIO

# Set up the LED pin
led_pin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

# Sensor data pin is connected to GPIO 4
sensor = adafruit_dht.DHT11(board.D4)

# Your ThingSpeak Channel ID and Write API Key
THINGSPEAK_CHANNEL_ID = 2640572
THINGSPEAK_API_KEY = "4N6U7YY8JQWCI32G"
THINGSPEAK_URL = f"https://api.thingspeak.com/channels/{THINGSPEAK_CHANNEL_ID}/fields/3.json?api_key={THINGSPEAK_API_KEY}&results=1"

while True:
    try:
        TS = requests.get(THINGSPEAK_URL)
        
        if TS.status_code == 200:
            response = TS.text
            data = json.loads(response)
            val = data['feeds'][0]['field3']
            
            if val != "0":
                GPIO.output(led_pin, GPIO.HIGH)
                print("LED is on")
            else:
                GPIO.output(led_pin, GPIO.LOW)
                print("LED is off")
            
            time.sleep(1)
            
        else:
            print(f"Failed to send data to ThingSpeak. Status code: {TS.status_code}")

    except KeyboardInterrupt:
        # Cleanup and exit when Ctrl+C is pressed
        print("Program interrupted.")
        GPIO.cleanup()
        break
