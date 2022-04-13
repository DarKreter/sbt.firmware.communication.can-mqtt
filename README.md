## Initialize can interface

Example usage:
```bash
python3 CanMQTT.py --can_socket vcan0 --mqtt_server pwraerospace.edu.pl --sbt_dbc ../miscellaneous.can-ids/SBT.dbc --kls_dbc ../miscellaneous.can-ids/KLS.dbc --thread 4G
```
To see arguments types:
```bash
python3 CanMQTT.py --help
```

Requirements:
```bash
sudo apt update
sudo apt install python3 python3-pip
pip3 install --requirement requirements.txt
git submodule update --init
```

With standard can to init just type:
```bash
sudo ip link set can0 up type can bitrate 250000
```

With virtual can to init type:
```bash
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set vcan0 up
```