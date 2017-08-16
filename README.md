# yzbxLib
useful demo code, scripts for ubuntu, windows and centos.

# centos system init
## config network
vi /etc/sysconfig/network-scripts/ifcfg-eth0
```
DEVICE=eth0
TYPE=Ethernet
ONBOOT=yes
BOOTPROTO=dhcp
IPV4_FAILURE_FATAL=yes
NAME="System eth0"
 ```
service network restart
