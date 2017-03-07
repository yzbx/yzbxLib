#!/bin/bash

while true
do
if [ ! `pgrep teamview` ] ; then
echo "yzb2.71828" | sudo -S /usr/bin/teamviewer daemon start
fi
sleep 30
done
