import gpiozero
import paho.mqtt.client as mqtt

# LED Setup using gpiozero
led = gpiozero.LED(4)

# Callback when a message is received
def on_message(client, userdata, message):
    payload = message.payload.decode()
    print(f"Received message: {payload}")
    if payload == "ON":
        led.on()  # Turn on the LED
    elif payload == "OFF":
        led.off()  # Turn off the LED

# MQTT Setup
broker_url = "test.mosquitto.org"  # Eclipse Mosquitto public broker
broker_port = 1883  # Default unencrypted MQTT port
topic = "group10/home/room/led"

client = mqtt.Client()
client.connect(broker_url, broker_port)
client.subscribe(topic)

client.on_message = on_message

# Start MQTT client loop
client.loop_start()

try:
    while True:
        pass  # Keep the script running
except KeyboardInterrupt:
    print("Experiment stopped")
finally:
    client.loop_stop()
