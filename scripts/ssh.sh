#!/usr/bin/expect
set timeout 10

spawn ssh -p 27174 root@192.243.113.196
expect "password:"
send "eG2C9QUXTCt6\r"
interact
