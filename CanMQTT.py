from __headers__ import *
from canReceiver import canReceiver, idle


class Direction(Enum):
    can2mqtt = 'can2mqtt'
    mqtt2can = 'mqtt2can'
    bidirectional = 'bidirectional'


# Call parameters
parser = argparse.ArgumentParser()
parser.add_argument("--can_socket", type=str,
                    help="can0 or vcan0", required=True)
parser.add_argument("--mqtt_server", type=str, required=True,
                    help="address of mqtt server ie. localhost or pwraerospace.edu.pl")
parser.add_argument("--sbt_dbc", type=str,
                    help="path to dbc file with SolarBoat IDs", required=True)
parser.add_argument("--kls_dbc", type=str,
                    help="path to dbc file with KLS frames", required=True)
parser.add_argument("--thread", type=str,
                    help="Thread in SBT/ to subscribe and to send", required=True)
parser.add_argument("--direction", type=Direction, choices=list(Direction), default=Direction.bidirectional,
                    help="direction of communication: \"can2mqtt\", \"mqtt2can\" or \"bidirectional\"")
args = parser.parse_args()

# Init can socket
can.rc['interface'] = 'socketcan'
can.rc['channel'] = args.can_socket
can.rc['bitrate'] = 250000
bus = Bus()

# config can decoder
canDecoder = CanDecoder(args.sbt_dbc, args.kls_dbc)

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
    except Exception as e:
        print("Error processing message: {}={}".format(topic, threadValue))
        print("Error: {}".format(e))
        print()


# config MQTT
myMQTT = MQTT(args.mqtt_server, 1883)
if args.direction == Direction.bidirectional or args.direction == Direction.mqtt2can:
    myMQTT.subscribe("SBT/{}/#".format(args.thread), callback)
# subscribe([("my/topic", 0), ("another/topic", 2)])
myMQTT.initConnection()


print("GO!")
if args.direction == Direction.can2mqtt or args.direction == Direction.bidirectional:
    canReceiver(bus, args, canDecoder, myMQTT)
else:
    idle()
