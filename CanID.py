import can
from can.interface import Bus
import cantools

class SbtCan:
    def __init__(self, dbcPath) -> None:
        self.db = cantools.database.load_file(dbcPath)
        self.arbitrationID = 0
        self.payload = bytearray()
        pass
    
    def decode_mess(self, id, payload):
        self.arbitrationID = id
        self.payload = payload
        self.data = self.db.decode_message(self.get_paramID(),payload)
        return self.data

    def get_paramID(self):
        return (self.arbitrationID & 0x3FFC0) >> 6

    def get_sourceID(self):
        return (self.arbitrationID & 0x3FC0000) >> 18
    
    def get_groupID(self):
        return (self.arbitrationID & 0x3F)

    def get_priority(self):
        return (self.arbitrationID & 0x1C000000) >> 26



