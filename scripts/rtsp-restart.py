# -*- coding: utf-8 -*-

# only for python2
import os,sys,datetime
import commands
import time

from multiprocessing import Pool

def run(device):
    print('python test-rtsp.py %s' % device)
    os.system('python test-rtsp.py %s' % device)

while True:
    pids=commands.getoutput('pgrep -f test-rtsp').split('\n')
    for pid in pids:
        print('kill %s'%pid)
        os.system('kill %s'%pid)

    devices=commands.getoutput('cat devices.txt').split('\n')
    p=Pool(len(devices))
    p.map(run,devices)

    time.sleep(60)

