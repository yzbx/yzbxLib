#!/bin/bash

while true
do
if [ ! `pgrep teamviewerd` ] ; then
echo "yzb2.71828" | sudo -S /usr/bin/teamviewer daemon start
fi
sleep 30
done
