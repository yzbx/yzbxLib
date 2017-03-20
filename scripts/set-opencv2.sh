#!/bin/bash

Root=/usr/local/opencv2
export LD_LIBRARY_PATH=$Root/lib
export PKG_CONFIG_PATH=$Root/lib/pkgconfig
export INCLUDE_PATH=$Root/include
export PYTHONPATH=${PYTHONEPATH}:$Root/lib/python2.7/dist-packages
