import paho.mqtt.client as mqtt

# MQTT settings
broker = "localhost"
port = 1883
topic = "home/temperature"

# Callback function when a message is received
def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()} on topic {message.topic}")


client = mqtt.Client()  # Create an MQTT client instance

client.on_message = on_message  # Assign callback function

client.connect(broker, port)  # Connect to the broker

client.subscribe(topic)  # Subscribe to the topic

client.loop_forever()  # Start listening for messages indefinitely
