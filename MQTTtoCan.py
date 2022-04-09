from __headers__ import *

# Call parameters
parser = argparse.ArgumentParser()
parser.add_argument("--can_socket", type=str, help="can0 or vcan0")
parser.add_argument("--mqtt_server", type=str,
                    help="address of mqtt server ie. localhost or pwraerospace.edu.pl")
parser.add_argument("--dbc_file", type=str, help="path to dbc file")
args = parser.parse_args()

# Init can socket
can.rc['interface'] = 'socketcan'
can.rc['channel'] = args.can_socket
can.rc['bitrate'] = 250000
bus = Bus()

# config can decoder
canDecoder = CanDecoder(args.dbc_file)

# The callback for when a PUBLISH message is received from the server.


def callback(topic, threadValue):
    keys = topic.split("/")

    extID = canDecoder.encode_arbitrationID(
        keys[len(keys) - 3], keys[len(keys) - 2])

    canPayload = canDecoder.encode_payload(
        keys[len(keys) - 2], keys[len(keys) - 1], threadValue)

    print("New message from MQTT!")
    print("Sending to CAN: {} = {}".format(topic, threadValue))
    print()
    bus.send(can.Message(arbitration_id=extID,
             data=canPayload, is_extended_id=True))


# config MQTT
myMQTT = MQTT(args.mqtt_server, 1883)
myMQTT.subscribe("#", callback)
myMQTT.initConnection()

print("GO!")

while 1:
    time.sleep(1)
    pass
