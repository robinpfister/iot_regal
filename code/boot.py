import network
import ntptime
import machine
import utime
from umqtt.simple import MQTTClient
from onewire import OneWire
import ujson

from bme import BME
from fan import Fan
from flowsensor import Flowsensor
from illumination import Illumination
from luminosity import Luminosity
from water_temperature import WaterTemperature
from bme_temp import BMETemp
from bme_humidity import BMEHumidity
from bme_voc_vsc import BMEVocVsc

class Regal:
    def __init__(self, wlan_config, mqtt_config, sensor_list, actor_list):
        """
         @wlan_config: {"ssid": "<your ssid>", "psswd": "<your password>"}
         @mqtt_config: {"server": "<mqtt server ip>", "client_id": "<your client name>", "user": "psswd": "<your user password>}
        """
        self.sensor_list = sensor_list
        self.actor_list = actor_list
        self.wlan_config = wlan_config
        self.do_connect()
        self.init_rtc_10()
        self.mqtt_config = mqtt_config
        self.init_mqtt_client()
        
    def do_connect(self):
        wlan = network.WLAN(network.WLAN.IF_STA)
        wlan.active(True)
        if not wlan.isconnected():
            print('connecting to network...')
            wlan.connect(self.wlan_config["ssid"], self.wlan_config["psswd"]) #Needs 
            while not wlan.isconnected():
                pass
        print('network config:', wlan.ipconfig('addr4'))
        self.wlan = wlan
        utime.sleep(5)
    
    def init_rtc_10(self):
        """
        Initialize RTC: After init, time can be received with current_time = utime.localtime().
        Retries up to 10 times in case of failure.
        """
        max_retries = 10
        rtc = machine.RTC()
        
        for attempt in range(1, max_retries + 1):
            try:
                ntptime.settime()
                print('Time successfully set to:', rtc.datetime())
                return  # Exit the function if time is set successfully
            except OSError as e:
                print(f'Attempt {attempt} failed to set time: {e}')
                if attempt < max_retries:
                    print('Retrying in 5 seconds...')
                    utime.sleep(5)  # Wait before retrying
        
        print('Failed to set time after 10 attempts.')
    
    def init_rtc(self):
        """
        initialize rtc: after init time can be received with current_time = utime.localtime()
        """
        # Set the time using NTP
        try:
            ntptime.settime()
            rtc = machine.RTC()
            print('Time set to:', rtc.datetime())
        except OSError as e:
            print('Failed to set time:', e)

    def init_mqtt_client(self):
        """create to client and connect"""
        # Connect to MQTT broker
        self.mqtt_client = MQTTClient(self.mqtt_config["client_id"], self.mqtt_config["server"], user=self.mqtt_config["user"], password=self.mqtt_config["psswd"])
        print(type(self.mqtt_client))
        self.mqtt_client.set_callback(self.on_message)
        self.mqtt_client.connect()
        print(f'Connected to {mqtt_config["server"]} MQTT broker')
        
        self.subscribe_actors()
        # Publish a message
        # message = b'Hello from MicroPython'
        # client.publish(topic, message)
        # print('Message published:', message)

    def subscribe_actors(self):
        for topic in actor_list.keys():
            self.mqtt_client.subscribe(topic)

    def publish_sensors(self):
        for topic, sensor in sensor_list.items():
            print(f"publishing {topic} for sensor {type(sensor)}")
            value = sensor.get_value()
            time_tuple = utime.localtime()
            # Format the time as "YYYY-MM-DD-HH:MM:SS"
            formatted_time = "{}-{:02d}-{:02d}-{:02d}:{:02d}:{:02d}".format(
                time_tuple[0], time_tuple[1], time_tuple[2],
                time_tuple[3], time_tuple[4], time_tuple[5]
            )
            payload = {
                "timestamp": formatted_time,
                "data": value
            }
            payload_json = ujson.dumps(payload)
            self.mqtt_client.publish(topic, payload_json)
            print(f"message published: \n{payload_json}")

    def on_message(self, topic, msg):
        print('Message received on %s: %s' % (topic, msg))
        self.actor_list[topic].set_value(msg)

    def run(self):
        # Wait for messages
        try:
            while True:
                print("awaiting messages")
                print(type(self.mqtt_client))
                self.mqtt_client.check_msg()
                utime.sleep(30)
                self.publish_sensors()
        finally:
            # Disconnect
            self.mqtt_client.disconnect()
            print('Disconnected from MQTT broker')
        

wlan_config = {
    "ssid": "X13OOLC", 
    "psswd": "9)8p592S"
    }


mqtt_config = {
    "server": "192.168.137.1", 
    "client_id": "dummy_regal",
    "user": "regal",
    "psswd": "iot_hydro"
    }


#TODO check i2c configuration pins
i2c_0 = machine.I2C(0, scl=machine.Pin(4), sda=machine.Pin(5)) #2xLicht (0x39, 0x29)
i2c_1 = machine.I2C(1, scl=machine.Pin(6), sda=machine.Pin(7)) #2xLicht (0x39, 0x29)

#TODO check one wire configuration and pins
one_wire_box = OneWire(machine.Pin(1))
one_wire_pipe = OneWire(machine.Pin(2))

addresses_pipes = {"Back" : bytearray(b'(\xffd\x1f[\xcd\xa3.'), #Red
                "Middle" : bytearray(b'(\xffd\x1f[\xa0\x1aS'), #Orange
                "Front" : bytearray(b"(\xd37\x1c\x91!\x06'")}  #Yellow

addresses_box = {"Left" : bytearray(b'(F\x19V\xb5\x01<\xd7'),  #Blue
                "Middle" : bytearray(b'(G&V\xb5\x01<\x0b'),   #White
                "Right" : bytearray(b'(\xffUV\xb5\x01<\x8e')} #Green

#map mqtt topic to sensor
bme_left_top = BME(i2c_1, 0x77)
bme_right_top = BME(i2c_1, 0x76)
bme_left_bottom = BME(i2c_0, 0x77)
bme_right_bottom = BME(i2c_0, 0x76)
sensor_list = {
    "Rack/Water/Temperature/Box/Left": WaterTemperature(one_wire_box, addresses_box["Left"]),
    "Rack/Water/Temperature/Box/Middle": WaterTemperature(one_wire_box, addresses_box["Middle"]), 
    "Rack/Water/Temperature/Box/Right": WaterTemperature(one_wire_box, addresses_box["Right"]), 
    "Rack/Air/Temperature/Top/Left": BMETemp(bme_left_top),
    "Rack/Air/Temperature/Top/Right": BMETemp(bme_right_top),
    "Rack/Air/Humidity/Top/Left": BMEHumidity(bme_left_top),
    "Rack/Air/Humidity/Top/Right": BMEHumidity(bme_left_top),
    "Rack/Brightness/Top/Left": Luminosity(i2c_0, 0x39),
    "Rack/Brightness/Top/Right": Luminosity(i2c_0, 0x29),
    "Rack/Brightness/Bottom/Left": Luminosity(i2c_1, 0x39),
    "Rack/Brightness/Bottom/Right": Luminosity(i2c_1, 0x29),
    "Rack/Air/VOC/Top/Left": BMEVocVsc(bme_left_top),
    "Rack/Air/VOC/Top/Right": BMEVocVsc(bme_right_top),
    "Rack/Water/Temperature/Pipe/Back": WaterTemperature(one_wire_pipe, addresses_pipes["Back"]),
    "Rack/Water/Temperature/Pipe/Middle": WaterTemperature(one_wire_pipe, addresses_pipes["Middle"]),
    "Rack/Water/Temperature/Pipe/Front": WaterTemperature(one_wire_pipe, addresses_pipes["Front"]),
    "Rack/Water/FlowRate/Pipe/Back": Flowsensor(40),
    "Rack/Water/FlowRate/Pipe/Middle": Flowsensor(41),
    "Rack/Water/FlowRate/Pipe/Front": Flowsensor(42),    
    # "Rack/Water/Temperature/PlantBox/Left": WaterTemperature(one_wire_box, addresses_box["Back"]),
    # "Rack/Water/Temperature/PlantBox/Middle": WaterTemperature(one_wire_box, addresses_box["Middle"]),
    # "Rack/Water/Temperature/PlantBox/Right": WaterTemperature(one_wire_box, addresses_box["Front"]),
    "Rack/Air/VOC/Bottom/Left": BMEVocVsc(bme_left_bottom),
    "Rack/Air/VOC/Bottom/Right": BMEVocVsc(bme_right_bottom),
    "Rack/Air/Temperature/Bottom/Left": BMETemp(bme_left_bottom),
    "Rack/Air/Temperature/Bottom/Right": BMETemp(bme_right_bottom),
    "Rack/Air/Humidity/Bottom/Left": BMEHumidity(bme_left_bottom),
    "Air/Humidity/Bottom/Right": BMEHumidity(bme_left_bottom)
}

    # New Topics because of middle
    # "Rack/Brightness/Bottom/Left": Luminosity(i2c_0, 0x39),
    # "Rack/Brightness/Bottom/Right": Luminosity(i2c_0, 0x29),
    # "Rack/Water/Temperature/PlantBox/Left": WaterTemperature(one_wire_pipe, addresses_box["Back"]),
    # "Rack/Water/Temperature/PlantBox/Middle": WaterTemperature(one_wire_pipe, addresses_box["Middle"]),
    # "Rack/Water/Temperature/PlantBox/Right": WaterTemperature(one_wire_pipe, addresses_box["Front"]),
    # "Rack/Air/VOC/Bottom/Left": BMEVocVsc(bme_left),
    # "Rack/Air/VOC/Bottom/Right": BMEVocVsc(bme_right),
    # "Rack/Air/Temperature/Bottom/Left": BMETemp(bme_left),
    # "Rack/Air/Temperature/Bottom/Right": BMETemp(bme_right),
    # "Rack/Air/Humidity/Bottom/Left": BMEHumidity(bme_left),
    # "Air/Humidity/Bottom/Right": BMEHumidity(bme_left)

    
    # Rack/VentilationControl
    # Rack/IlluminationControl

actor_list = {
    b'Rack/VentilationControl': Fan("<insert pin here>"),
    b'Rack/IlluminationControl': Illumination("<insert pin here>")
}

regal = Regal(wlan_config=wlan_config, mqtt_config=mqtt_config, sensor_list=sensor_list, actor_list=actor_list)
regal.run()
