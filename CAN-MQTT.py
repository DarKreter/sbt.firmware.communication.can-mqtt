from __headers__ import *

class Direction(Enum):
    can2mqtt = 'can2mqtt'
    mqtt2can = 'mqtt2can'
    bidirectional = 'bidirectional'

# Call parameters
parser = argparse.ArgumentParser()
parser.add_argument("--can_socket", type=str, help="can0 or vcan0")
parser.add_argument("--mqtt_server", type=str,
                    help="address of mqtt server ie. localhost or pwraerospace.edu.pl")
parser.add_argument("--dbc_file", type=str, help="path to dbc file")
parser.add_argument("--direction", type=Direction, choices=list(Direction),
                    help="direction of communication: \"can2mqtt\", \"mqtt2can\" or \"bidirectional\"")
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
    try:
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
    except:
        print("Error processing message: {}={}".format(topic, threadValue))

# config MQTT
myMQTT = MQTT(args.mqtt_server, 1883)
if args.direction == Direction.bidirectional or args.direction == Direction.mqtt2can:
    myMQTT.subscribe("#", callback)
# subscribe([("my/topic", 0), ("another/topic", 2)])
myMQTT.initConnection()


def idle():
    while 1:
        time.sleep(1)
        pass


def canReceiver():
    while 1:
        for msg in bus:
            try:
                # Decode frame
                frame = canDecoder.decode_payload(msg.arbitration_id, msg.data)

                # Get SBT IDs
                sourceIDname = sourceIDtoName[canDecoder.decode_sourceID(
                    msg.arbitration_id)]
                paramIDname = paramIDtoName[canDecoder.decode_paramID(
                    msg.arbitration_id)]

                print("New message from CAN!")
                # Print all signals from frame to MQTT
                for signal in frame:
                    myMQTT.publish(
                        [sourceIDname, paramIDname, signal], frame[signal])
                    print("Sending to MQTT: {}/{}/{} = {}".format(sourceIDname,
                                                                  paramIDname, signal, frame[signal]))
                print()
            except:
                print("Unknown frame: {}#{}".format(msg.arbitration_id, msg.data))


print("GO!")

if args.direction == Direction.can2mqtt or args.direction == Direction.bidirectional:
    canReceiver()
else:
    idle()
