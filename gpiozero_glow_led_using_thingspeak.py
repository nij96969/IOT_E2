import time
import board
import adafruit_dht
import requests
import json
from gpiozero import LED

# Set up the LED using gpiozero
led = LED(21)  # Pin 21 for the LED

# Sensor data pin is connected to GPIO 4
sensor = adafruit_dht.DHT11(board.D4)

# Your ThingSpeak Channel ID and Write API Key
THINGSPEAK_CHANNEL_ID = "2641847"
THINGSPEAK_API_KEY = "HDT7IFAH6Y2H0N7D"
THINGSPEAK_URL = f"https://api.thingspeak.com/channels/2641847/fields/1.json?api_key=HDT7IFAH6Y2H0N7D&results=1"

while True:
    try:
        TS = requests.get(THINGSPEAK_URL)
        
        if TS.status_code == 200:
            response = TS.text
            data = json.loads(response)
            #print(data)
            val = data['feeds'][0]['field1']
            print("val :: ",val)
            if val != "0":
                led.on()  # Turn on the LED
                print("LED is on")
            else:
                led.off()  # Turn off the LED
                print("LED is off")
            
            time.sleep(1)
            
        else:
            print(f"Failed to send data to ThingSpeak. Status code: {TS.status_code}")

    except KeyboardInterrupt:
        # Cleanup and exit when Ctrl+C is pressed
        print("Program interrupted.")
        break
