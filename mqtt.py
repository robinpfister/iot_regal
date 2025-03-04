import network
import ntptime
import machine
import utime
from umqtt.simple import MQTTClient

def do_connect():
    wlan = network.WLAN(network.WLAN.IF_STA)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('X13OOLC', '9)8p592S') #Needs 
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ipconfig('addr4'))
    
def set_rtc():
    # Set the time using NTP
    try:
        ntptime.settime()
        rtc = machine.RTC()
        print('Time set to:', rtc.datetime())
    except OSError as e:
        print('Failed to set time:', e)

    # Print the current time
    #while True:
    #    current_time = utime.localtime()
    #   print('Current time:', current_time)
    #   utime.sleep(60)  # Update every 60 seconds

def test_mqtt():
    # MQTT settings
    mqtt_server = '192.168.137.1'
    client_id = 'dummy_regal'
    usern='regal'
    passwd='iot_hydro'
    topic = b'test/topic'

    # Connect to MQTT broker
    client = MQTTClient(client_id, mqtt_server, user=usern, password=passwd)
    client.connect()
    print('Connected to %s MQTT broker' % mqtt_server)

    # Publish a message
    message = b'Hello from MicroPython'
    client.publish(topic, message)
    print('Message published:', message)

    # Disconnect
    client.disconnect()
    print('Disconnected from MQTT broker')
    
def mqtt_ping_pong():
    #MQTT config   
    mqtt_server = '192.168.137.1'
    client_id = 'dummy_regal'
    usern='regal'
    passwd='iot_hydro'
   
    pub_topic = b'ping_topic'
    sub_topic = b'pong_topic'

    # Callback function for when a message is received
    def sub_callback(topic, msg):
        print('Message received on %s: %s' % (topic, msg))
        if msg == b'pong':
            client.publish(pub_topic, b'ping')
            print('Ping sent')

    # Connect to MQTT broker
    client = MQTTClient(client_id, mqtt_server, user=usern, password=passwd)
    client.set_callback(sub_callback)
    client.connect()
    print('Connected to %s MQTT broker' % mqtt_server)

    # Subscribe to the topic
    client.subscribe(sub_topic)
    print('Subscribed to topic:', sub_topic)

    # Send the initial ping message
    client.publish(pub_topic, b'ping')
    print('Initial ping sent')

    # Wait for messages
    try:
        while True:
            client.wait_msg()
            utime.sleep(5)
    finally:
        # Disconnect
        client.disconnect()
        print('Disconnected from MQTT broker')


do_connect()
set_rtc()
#test_mqtt()
mqtt_ping_pong()