sourceID = 0x07
paramID = 0x009
groupID = 2
priority = 5

arbitrationID = (((priority & 0x07) << 26) |
                 ((sourceID & 0xFF) << 18) |
                 ((paramID & 0x0FFF) << 6) |
                 ((groupID) & 0x3F))

print(hex(arbitrationID))
