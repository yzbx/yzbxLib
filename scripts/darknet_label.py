# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import os
import sys
from os import getcwd
import random

image_sets = ['n01986806', 'crab', 'crab_20170620']

sets = []
for image_set in image_sets:
    sets.append(('train', image_set))
    sets.append(('test', image_set))

# sets=[('train','n01986806'),('test','n01986806'),('train','crab'),('test','crab'),('train','crab_20170620'),('test','crab_20170620')]

# maybe need convert the xml object name
classes = [u'crab', u'n01986806']


def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_annotation(image_set, image_id):
    in_file = open('Annotations/%s/%s.xml' % (image_set, image_id))

    out_file_name = ('labels/%s/%s.txt' % (image_set, image_id))
    out_file_name = out_file_name.replace('images', 'labels')
    out_file_name = out_file_name.replace('JPEGImages', 'labels')
    out_file = open(out_file_name, 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    # print('in_file is ',in_file)
    for obj in root.iter('object'):
        # difficult = obj.find('Difficult').text
        # difficult = obj.find('difficult').text
        difficult = 0
        cls = obj.find('name').text

        if cls.find('crab') != -1:
            cls = u'crab'

        if cls not in classes or int(difficult) == 1:
            print('error cls: ', cls)
            continue

        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


# /media/sdb/ISCAS_Dataset/helmet_seatbelt
wd = getcwd()
img_formats = ['jpg', 'JPG', 'png', 'PNG', 'jpeg', 'JPEG']

# create train_xxx.txt,test_xxx.txt
for image_set in image_sets:
    xmls = []
    for f in os.listdir('Annotations/%s' % image_set):
        filename = os.path.join('Annotations/%s' % image_set, f)
        if os.path.isfile(filename) and f.find('.xml') != -1:
            xmls.append(f)

    random.shuffle(xmls)
    datasize = len(xmls)
    train_size = int(datasize * 0.7)
    train_txt = open('config/%s_%s.txt' % ('train', image_set), 'w')
    test_txt = open('config/%s_%s.txt' % ('test', image_set), 'w')

    for i in range(datasize):
        if i < train_size:
            train_txt.write('%s\n' % (xmls[i]))
        else:
            test_txt.write('%s\n' % (xmls[i]))

    train_txt.close()
    test_txt.close()

# use train_xxx.txt test_xxx.txt to create labels/xxx.txt, list_train_xxx.txt, list_test_xxx.txt

for data_type, image_set in sets:
    if not os.path.exists('labels/%s' % (image_set)):
        os.makedirs('labels/%s' % (image_set))
    image_ids = open('config/%s_%s.txt' % (data_type, image_set)).read().strip().split()
    list_file = open('config/list_%s_%s.txt' % (data_type, image_set), 'w')
    for image in image_ids:
        image_id = image.replace('.jpg', '')
        for fmt in img_formats:
            image_id = image_id.replace('.%s' % fmt, '')

        image_id = image_id.replace('.xml', '')

        abs_img_path = ''
        for fmt in img_formats:
            abs_img_path = ('%s/JPEGImages/%s/%s.%s' % (wd, image_set, image_id, fmt))
            if os.path.exists(abs_img_path):
                break

        if not os.path.exists(abs_img_path):
            print('warning cannot find image', abs_img_path)
            continue

        list_file.write('%s\n' % (abs_img_path))
        convert_annotation(image_set, image_id)
    list_file.close()

os.system("cat config/list_train_*.txt > config/train.txt")
os.system("cat config/list_test_*.txt > config/test.txt")
