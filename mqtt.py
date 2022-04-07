#!/usr/bin/python3
import paho.mqtt.client as paho

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code " + str(rc))

mqtt_server_host = "pwraerospace.edu.pl"
mqtt_server_port = 1883

my_mqtt_client = paho.Client()
my_mqtt_client.on_connect = on_connect
my_mqtt_client.connect(mqtt_server_host, mqtt_server_port)

my_mqtt_client.publish("test/a", 12)