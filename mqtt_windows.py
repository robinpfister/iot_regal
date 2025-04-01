import paho.mqtt.client as mqtt
import time

# MQTT settings
mqtt_server = 'localhost'
mqtt_port = 1883  # Change to 8883 for TLS/SSL
username = 'regal'
password = 'iot_hydro'
pub_topic = 'pong_topic'
sub_topic = 'ping_topic'

# Callback function for when a message is received
def on_message(client, userdata, message):
    print('Message received on topic %s: %s' % (message.topic, message.payload.decode()))
    if message.payload.decode() == 'ping':
        client.publish(pub_topic, 'pong')
        print('Pong sent')

# Create MQTT client
client = mqtt.Client()

# Set username and password
client.username_pw_set(username, password)

# Assign the callback function
client.on_message = on_message

# Connect to the MQTT broker
client.connect(mqtt_server, mqtt_port, 60)

# Start the client loop
client.loop_start()

# Subscribe to the topic
# client.subscribe(sub_topic)
# print('Subscribed to topic:', sub_topic)

# Wait for messages
try:
    while True:
        time.sleep(10)
        client.publish("Time","2025-03-25-10:00:00")
finally:
    # Stop the client loop and disconnect
    client.loop_stop()
    client.disconnect()
    print('Disconnected from MQTT broker')
