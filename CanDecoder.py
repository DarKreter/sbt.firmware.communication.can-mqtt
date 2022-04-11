import can
from can.interface import Bus
import cantools
from CanID_autogenerated import *


class CanDecoder:
    def __init__(self, dbcPath) -> None:
        self.db = cantools.database.load_file(dbcPath)
        pass

    def decode_payload(self, id, payload):
        self.data = self.db.decode_message(self.decode_paramID(id), payload)
        return self.data

    def decode_paramID(self, arbitrationID):
        return (arbitrationID & 0x3FFC0) >> 6

    def decode_sourceID(self, arbitrationID):
        return (arbitrationID & 0x3FC0000) >> 18

    def decode_groupID(self, arbitrationID):
        return (arbitrationID & 0x3F)

    def decode_priority(self, arbitrationID):
        return (arbitrationID & 0x1C000000) >> 26

    def encode_arbitrationID(self, sourceID_str, paramID_str):
        sourceID = nameToSourceID[sourceID_str]
        paramID = nameToParamID[paramID_str]['ParamID']
        groupID = nameToParamID[paramID_str]['GroupID']
        priority = nameToParamID[paramID_str]['Priority']

        arbitrationID = (((priority & 0x07) << 26) |
                         ((sourceID & 0xFF) << 18) |
                         ((paramID & 0x0FFF) << 6) |
                         ((groupID) & 0x3F))

        return arbitrationID

    def encode_payload(self, paramIDname, signalName, signalValue):

        mess = self.db.get_message_by_name(paramIDname)
        signals = dict()

        x = False
        for signal in mess.signals:
            if signalName == signal.name:
                signals[signal.name] = float(signalValue)
                x = True
            else:
                signals[signal.name] = 0

        if x == False:
            raise

        return mess.encode(signals)
    

    def decode_sourceID_name(self, arbitrationID):
        if arbitrationID == 0x0CF11E05 or arbitrationID == 0x0CF11F05:
            return "KLS"
        else:
            return sourceIDtoName[self.decode_sourceID(arbitrationID)]

    def decode_paramID_name(self, arbitrationID):
        if arbitrationID == 0x0CF11E05:
            return "KLS_DATA_1"
        elif arbitrationID == 0x0CF11F05:
            return "KLS_DATA_2"
        else:
            return paramIDtoName[self.decode_paramID(arbitrationID)]