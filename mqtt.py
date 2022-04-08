#!/usr/bin/python3
import paho.mqtt.client as paho

class MQTT:  
    def __init__(self, server_host, server_port) -> None:
        self.server_host = server_host
        self.server_port = server_port
        self.__subscribePattern = ""
        
    def subscribe(self, subscribePattern, receive_callback):
        self.__subscribePattern = subscribePattern
        self.__receive_callback = receive_callback

    def initConnection(self):
        self.mqtt_client = paho.Client("SBT", protocol=paho.MQTTv5)

        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_message = self.on_message

        self.mqtt_client.connect(self.server_host, self.server_port)
        self.mqtt_client.loop_start()

    def publish(self, threads, value):
        mqtt_thread = "/".join(threads)
        
        self.mqtt_client.publish(mqtt_thread, value)

    def on_connect(self, client, userdata, flags, rc, mqttv5_data: None):
        print("Connected with result code {}".format(str(rc)))

        if self.__subscribePattern != "":
            self.mqtt_client.subscribe((self.__subscribePattern, paho.SubscribeOptions(noLocal=True)))
            # subscribe(self.__subscribePattern)

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        self.__receive_callback(msg.topic, msg.payload)