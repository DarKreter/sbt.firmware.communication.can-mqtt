#!/usr/bin/python3
import paho.mqtt.client as paho

class MQTT:
    @staticmethod
    def on_connect(client, userdata, flags, rc):
        print("Connected to MQTT broker with result code " + str(rc))
    
    def __init__(self, server_host, server_port) -> None:
        self.mqtt_client = paho.Client()
        self.mqtt_client.on_connect = staticmethod(self.on_connect)
        self.mqtt_client.connect(server_host, server_port)

    def Publish(self, threads, value):
        mqtt_thread = "/".join(threads)
        
        self.mqtt_client.publish(mqtt_thread, value)
