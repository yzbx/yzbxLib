# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

sets=[('train','helmet'),('test','helmet'),('train','seatbelt'),('test','seatbelt')]

classes = [u'\u5b89\u5168\u5e3d', u'\u4eba', u'\u5b89\u5168\u5e26']


def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(image_set,image_id):
    in_file = open('%s/Annotations/%s.xml'%(image_set, image_id))
    out_file = open('%s/labels/%s.txt'%(image_set,image_id), 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            print('error cls: ',cls)
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

# /media/sdb/ISCAS_Dataset/helmet_seatbelt
wd = getcwd()

for data_type,image_set in sets:
    if not os.path.exists('%s/labels/'%(image_set)):
        os.makedirs('%s/labels/'%(image_set))
    image_ids = open('%s/%s.txt'%(image_set, data_type)).read().strip().split()
    list_file = open('%s_%s.txt'%(data_type,image_set), 'w')
    for image in image_ids:
        image_id=image.replace('.jpg','')
        image_id=image_id.replace('.xml','')
        list_file.write('%s/%s/JPEGImages/%s.jpg\n'%(wd, image_set, image_id))
        convert_annotation(image_set,image_id)
    list_file.close()

#os.system("cat 2007_train.txt 2007_val.txt 2012_train.txt 2012_val.txt > train.txt")
#os.system("cat 2007_train.txt 2007_val.txt 2007_test.txt 2012_train.txt 2012_val.txt > train.all.txt")

