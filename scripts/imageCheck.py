# -*- coding: utf-8 -*-

import cv2
import sys,os

if len(sys.argv) < 2:
    print('usage: python imageCheck.py xxx-dir')
    sys.exit(-1)

dir=sys.argv[1]

if not os.path.isdir(dir):
    print('%s is invalid directory'%dir)


for f in os.listdir(dir):
    file=os.path.join(dir,f)
    if os.path.isfile(file):
        img=cv2.imread(file)
        if type(img) == type(None):
            print('remove file ',file)
            os.remove(file)
        else:
            print('file %s: type is %s, shape is %s'%(file,type(img),img.shape))