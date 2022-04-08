sourceIDtoName = dict()
sourceIDtoName[1] = "MPPT_CONTROLLER_1"
sourceIDtoName[2] = "MPPT_CONTROLLER_2"
sourceIDtoName[3] = "LIFEPO4_CONTROLLER_1"
sourceIDtoName[4] = "LIFEPO4_CONTROLLER_2"
sourceIDtoName[5] = "MPPT_1"
sourceIDtoName[6] = "MPPT_2"
sourceIDtoName[7] = "MPPT_3"
sourceIDtoName[8] = "MPPT_4"
sourceIDtoName[9] = "LIFEPO4_1"
sourceIDtoName[10] = "LIFEPO4_2"
sourceIDtoName[11] = "LIFEPO4_3"
sourceIDtoName[12] = "LIFEPO4_4"
sourceIDtoName[13] = "PUMPS_CONTROLLER"
sourceIDtoName[14] = "CPB_CONTROLLER"
sourceIDtoName[15] = "PiBox"
sourceIDtoName[16] = "GPS_CONTROLLER"

nameToSourceID = dict()
nameToSourceID["MPPT_CONTROLLER_1"] = 1
nameToSourceID["MPPT_CONTROLLER_2"] = 2
nameToSourceID["LIFEPO4_CONTROLLER_1"] = 3
nameToSourceID["LIFEPO4_CONTROLLER_2"] = 4
nameToSourceID["MPPT_1"] = 5
nameToSourceID["MPPT_2"] = 6
nameToSourceID["MPPT_3"] = 7
nameToSourceID["MPPT_4"] = 8
nameToSourceID["LIFEPO4_1"] = 9
nameToSourceID["LIFEPO4_2"] = 10
nameToSourceID["LIFEPO4_3"] = 11
nameToSourceID["LIFEPO4_4"] = 12
nameToSourceID["PUMPS_CONTROLLER"] = 13
nameToSourceID["CPB_CONTROLLER"] = 14
nameToSourceID["PiBox"] = 15
nameToSourceID["GPS_CONTROLLER"] = 16


paramIDtoName = dict()
paramIDtoName[1] = "HEARTBEAT"
paramIDtoName[2] = "LIFEPO4_GENERAL"
paramIDtoName[3] = "LIFEPO4_CELLS_1"
paramIDtoName[4] = "LIFEPO4_CELLS_2"
paramIDtoName[5] = "LIFEPO4_CELLS_3"
paramIDtoName[6] = "PUMPS_GENERAL"
paramIDtoName[7] = "EMBEDDED_BUS_DATA"
paramIDtoName[8] = "POWER_BUS_DATA"
paramIDtoName[9] = "PV_DATA"
paramIDtoName[10] = "MPPT_CHARGER_DATA"
paramIDtoName[11] = "YIELD_DATA"
paramIDtoName[12] = "GEODETIC_POSITION_1"
paramIDtoName[13] = "GEODETIC_POSITION_2"
paramIDtoName[14] = "NED_VELOCITY"
paramIDtoName[15] = "NED_HEADING"


nameToParamID = dict()
nameToParamID["HEARTBEAT"] = {'GroupID': 0, 'ParamID': 1, 'Priority': 0}
# nameToParamID["LIFEPO4_GENERAL"] = 2
# nameToParamID["LIFEPO4_CELLS_1"] = 3
# nameToParamID["LIFEPO4_CELLS_2"] = 4
# nameToParamID["LIFEPO4_CELLS_3"] = 5
nameToParamID["PUMPS_GENERAL"] = {'GroupID': 0, 'ParamID': 6, 'Priority': 0}
# nameToParamID["EMBEDDED_BUS_DATA"] = 7
# nameToParamID["POWER_BUS_DATA"] = 8
# nameToParamID["PV_DATA"] = 9
# nameToParamID["MPPT_CHARGER_DATA"] = 10
# nameToParamID["YIELD_DATA"] = 11
# nameToParamID["GEODETIC_POSITION_1"] = 12
# nameToParamID["GEODETIC_POSITION_2"] = 13
# nameToParamID["NED_VELOCITY"] = 14
# nameToParamID["NED_HEADING"] = 15

groupIDtoName = dict()
groupIDtoName["LIFEPO4_DATA"] = 1
groupIDtoName["MPPT_DATA"] = 2

nameToGroupID = dict()
nameToGroupID[1] = "LIFEPO4_DATA"
nameToGroupID[2] = "MPPT_DATA"
