from __headers__ import *


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
parser.add_argument("--dbc_file", type=str,
                    help="path to dbc file", required=True)
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
canDecoder = CanDecoder(args.dbc_file)


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
