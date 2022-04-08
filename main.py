import can
from can.interface import Bus
import cantools
from CanDecoder import CanDecoder
from CanID_autogenerated import *
from mqtt import MQTT

# Call parameters
dbcPath = '../miscellaneous.can-ids/SBT.dbc'

# Init can socket
can.rc['interface'] = 'socketcan'
can.rc['channel'] = 'vcan0'
can.rc['bitrate'] = 250000
bus = Bus()

# config can decoder
canDecoder = CanDecoder(dbcPath)

# config MQTT
myMQTT = MQTT("pwraerospace.edu.pl", 1883)


print("GO!")

while 1:
    for msg in bus:
        # Decode frame
        frame = canDecoder.decode_mess(msg.arbitration_id, msg.data)

        # Get SBT IDs
        sourceIDname = sourceIDtoName[canDecoder.get_sourceID()]
        paramIDname = paramIDtoName[canDecoder.get_paramID()]

        # Print all signals from frame to MQTT
        for signal in frame:
            myMQTT.Publish([sourceIDname, paramIDname, signal], frame[signal])
            print("{}/{}/{} = {}".format(sourceIDname, paramIDname, signal, frame[signal]))










