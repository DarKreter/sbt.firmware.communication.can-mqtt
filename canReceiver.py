from __headers__ import *


def canReceiver(bus, args, canDecoder, myMQTT):
    while 1:
        for msg in bus:
            try:
                # Decode frame
                frame = canDecoder.decode_payload(msg.arbitration_id, msg.data)

                # Get SBT IDs
                sourceIDname = canDecoder.decode_sourceID_name(msg.arbitration_id)
                paramIDname = canDecoder.decode_paramID_name(msg.arbitration_id)

                print("New message from CAN!")
                # Print all signals from frame to MQTT
                for signal in frame:
                    signalValue = "{:.3f}".format(frame[signal])
                    myMQTT.publish(
                        ["SBT", args.thread, sourceIDname, paramIDname, signal], signalValue)
                    print("Sending to MQTT: SBT/{}/{}/{}/{} = {}".format(args.thread, sourceIDname,
                                                                         paramIDname, signal, signalValue))
                print()

            except Exception as e:
                print("Unknown frame: {}#{}".format(
                    msg.arbitration_id, msg.data))
                print("Error: {}".format(e))
                print()


def idle():
    while 1:
        time.sleep(1)
        pass
