#!/usr/bin/expect
set timeout 10

spawn ssh -p 28142 root@45.78.18.96
expect "password:"
send "ccfjEEHEXdTM\r"
interact
