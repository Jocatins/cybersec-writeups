Ping Sweep --> ifconfig -c 1 [one packet of data count]

ping 10.5.5.1 -c 1 > ~/ip.txt
cat ~/ip.txt | grep "64 bytes"
cat ip.txt | grep "64 bytes" | cut -d " " -f 4
cat ip.txt | grep "64 bytes" | cut -d " " -f 4 | tr -d ":"

mouspad ipsweep.sh

dilimeter ->space

#!/bin/bash

if [ "$1" == "" ]
then
    echo "You forgot an IP address"
    echo "Syntax: ./ipsweep.sh 10.5.5"
else
    for ip in $(seq 1 254); do
        ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
    done
fi

run in this order ==>

chmod +x ipsweep.sh

./ipsweep.sh 10.5.5
10.5.5.1
10.5.5.11
10.5.5.12
10.5.5.13

nmap 10.5.5.1 10.5.5.11 10.5.5.12 10.5.5.13

nc -nvlp 7777