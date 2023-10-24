# -*- coding: utf-8 -*-
"""
check dateset and annotations!
input: image + xml
output: annotated image
"""
import xml.etree.ElementTree as ET
import cv2
import sys

def check(image,xml):
    cvimg=cv2.imread(image)
    if type(cvimg) == type(None):
        print('cannot open file %s'%image)

    tree = ET.parse(xml)
    root = tree.getroot()
    objects=root.findall('object')

    h,w,c=cvimg.shape
    bboxes=[]
    for object in objects:
        bndboxes=object.findall('bndbox')
        name=object.find('name').text
        for bndbox in bndboxes:
            xmin=int(bndbox.find('xmin').text)
            xmax=int(bndbox.find('xmax').text)
            ymin=int(bndbox.find('ymin').text)
            ymax=int(bndbox.find('ymax').text)

            bboxes.append({"name":name,"xmin":xmin,"xmax":xmax,"ymin":ymin,"ymax":ymax})

            cv2.rectangle(cvimg,(xmin,ymin),(xmax,ymax),(255,0,0),thickness=5)
            cv2.putText(cvimg,name,(xmin,max(ymin-20,0)),0,1e-3*h,(255,255,0))

    cv2.namedWindow("image",cv2.WINDOW_NORMAL)
    cv2.imshow('image',cvimg)
    cv2.waitKey(0)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('usage: pythone xxx.py xxx.xml xxx.jpg')
        sys.exit(-1)

    if sys.argv[2].find('xml') != -1:
        check(image=sys.argv[1],xml=sys.argv[2])
    elif sys.argv[1].find('xml') !=-1:
        check(image=sys.argv[2],xml=sys.argv[1])
    else:
        print('usage: pythone xxx.py xxx.xml xxx.jpg')
        sys.exit(-1)
