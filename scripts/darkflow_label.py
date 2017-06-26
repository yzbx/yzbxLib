# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join, isfile

sets = ['helmet0', 'helmet1', 'helmet2', 'seatbelt']
subdirs = ['Annotations', 'JPEGImages']
saveto = 'english'
for dir in subdirs:
    savedir = os.path.join(saveto, dir)
    if not os.path.exists(saveto):
        os.mkdir(saveto)
    if not os.path.exists(savedir):
        os.mkdir(savedir)

i = 1
for set in sets:
    dir = os.path.join(set, subdirs[0])
    for f in os.listdir(dir):
        if f.find('xml') != -1:
            ann_file = os.path.join(dir, f)
            img_file = ann_file.replace(subdirs[0], subdirs[1])
            img_file = img_file.replace('xml', 'jpg')

            new_ann_file = os.path.join(saveto, subdirs[0], '%d.xml' % i)
            new_img_file = new_ann_file.replace(subdirs[0], subdirs[1])
            new_img_file = new_img_file.replace('xml', 'jpg')

            img_basename = os.path.basename(new_img_file)

            # convert xml file to standard voc format, set the correct file and pathname
            tree = ET.parse(ann_file)
            path = tree.find('path')
            path.text = 'Unknow'
            folder = tree.find('folder')
            folder.text = 'Unknow'
            filename = tree.find('filename')
            filename.text = img_basename

            # change Chinese name to english
            objs = tree.findall('object')
            for obj in objs:
                name = obj.find('name')
                if name.text == u'&#20154;' or name.text == u'人' or name.text == 'person':
                    name.text = 'person'
                elif name.text == u'&#23433;&#20840;&#24102;' or name.text == u'安全带' or name.text == 'Safety belt':
                    name.text = 'seatbelt'
                elif name.text == u'&#23433;&#20840;&#24125;' or name.text == u'安全帽' or name.text == 'Safety hat':
                    name.text = 'helmet'
                else:
                    print('unknow name %s' % name.text)
            tree.write(new_ann_file)
            os.system('cp %s %s' % (img_file, new_img_file))

            print('image is %s' % new_img_file)
            print('annotation is %s' % new_ann_file)
            i = i + 1

