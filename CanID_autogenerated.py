
paramIDtoName = dict()
paramIDtoName[1] = "HEARTBEAT"
paramIDtoName[2] = "LIFEPO4_GENERAL"
paramIDtoName[3] = "LIFEPO4_CELLS_1"
paramIDtoName[4] = "LIFEPO4_CELLS_2"
paramIDtoName[5] = "LIFEPO4_CELLS_3"
paramIDtoName[6] = "PUMPS_GENERAL"
paramIDtoName[7] = "EMBEDDED_BUS_DATA"

nameToParamID = dict()
paramIDtoName["HEARTBEAT"] = 1
paramIDtoName["LIFEPO4_GENERAL"] = 2
paramIDtoName["LIFEPO4_CELLS_1"] = 3
paramIDtoName["LIFEPO4_CELLS_2"] = 4
paramIDtoName["LIFEPO4_CELLS_3"] = 5
paramIDtoName["PUMPS_GENERAL"] = 6
paramIDtoName["EMBEDDED_BUS_DATA"] = 7

sourceIDtoName = dict()
sourceIDtoName[1] = "MPPT_CONTROLLER_1"
sourceIDtoName[2] = "MPPT_CONTROLLER_2"
sourceIDtoName[3] = "LIFEPO4_CONTROLLER_1"
sourceIDtoName[4] = "LIFEPO4_CONTROLLER_2"
sourceIDtoName[5] = "MPPT_1"
sourceIDtoName[6] = "MPPT_2"
sourceIDtoName[7] = "MPPT_3"
sourceIDtoName[8] = "MPPT_4"

nameToSourceID = dict()
nameToSourceID["MPPT_CONTROLLER_1"] = 1
nameToSourceID["MPPT_CONTROLLER_2"] = 2
nameToSourceID["LIFEPO4_CONTROLLER_1"] = 3
nameToSourceID["LIFEPO4_CONTROLLER_2"] = 4
nameToSourceID["MPPT_1"] = 5
nameToSourceID["MPPT_2"] = 6
nameToSourceID["MPPT_3"] = 7
nameToSourceID["MPPT_4"] = 8

groupIDtoName = dict()
groupIDtoName["LIFEPO4_DATA"] = 1
groupIDtoName["MPPT_DATA"] = 2

nameToGroupID = dict()
nameToGroupID[1] = "LIFEPO4_DATA"
nameToGroupID[2] = "MPPT_DATA"
