#!/bin/bash

ps -auxf | head -1
ps -auxf | sort -k3 -nr| head -3
