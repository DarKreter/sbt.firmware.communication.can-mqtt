#!/usr/bin/python3

#Based on what Kacper Chmielewski created in pwrsbt-python-kls/main.py
#To init CAN use: sudo ip link set can0 up type can bitrate 1000000
import struct
import myCAN
from can.interface import Bus

myCAN.rc['interface'] = 'socketcan_native'
myCAN.rc['channel'] = 'can0'
myCAN.rc['bitrate'] = 250000

bus = Bus()


print("GO!")

while 1:
    for msg in bus:
        print(hex(msg.arbitration_id))
        print(msg.data)
        print()
        
#        idToFilter = 0x000C0040
#        if msg.arbitration_id == idToFilter:
        
#            upTime = int.from_bytes(msg.data[0:4], byteorder='little', signed=False)
#            TxFail = int.from_bytes(msg.data[4:5], byteorder='little',signed=False)
#            RxFail = int.from_bytes(msg.data[5:6], byteorder='little',signed=False)
#            print("UpTime: " + str(upTime) + "ms")
#            print("TxFail: " + str(TxFail))
#            print("RxFail: " + str(RxFail))
#if data is float
        #dane = struct.unpack('f', msg.data[0:4])
        #print("Dane: " + str(dane[0]))
