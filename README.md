## Initialize can interface

To init can just type:
```bash
sudo ip link set can0 up type can bitrate 250000
```
canToMQTT.py and MQTTtoCan.py should NOT be used together, because of infinite communication loop

If you want to create bidirectional communication just use CAN-MQTT.py
