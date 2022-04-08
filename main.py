import can
from can.interface import Bus
import cantools
from CanID import SbtCan


dbcPath = '../miscellaneous.can-ids/SBT.dbc'

canDecoder = SbtCan(dbcPath)
frame = canDecoder.decode_mess(0xc0040, bytearray(b'\xc8y\t\x00\x00\x00\x00\x00'))

print(canDecoder.get_paramID())
print(canDecoder.get_sourceID())
print(canDecoder.get_groupID())
print(canDecoder.get_priority())


for signal in frame:
    print("{} = {}".format(signal, frame[signal]))
