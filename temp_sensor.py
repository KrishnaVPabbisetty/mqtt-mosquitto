import paho.mqtt.client as mqtt
import random
import time

# MQTT settings
broker = "localhost"
port = 1883
topic = "home/temperature"

# Create an MQTT client instance
client = mqtt.Client()

# Connect to the broker
client.connect(broker, port)

# Publish temperature readings every second
while True:
    temperature = round(random.uniform(20.0, 30.0), 2)
    print(f"Publishing temperature: {temperature}")
    client.publish(topic, temperature)
    time.sleep(1)
