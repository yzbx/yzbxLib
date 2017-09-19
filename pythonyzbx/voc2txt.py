# -*- coding: utf-8 -*-
'''
convert voc xml to txt format
filepath,x1,y1,x2,y2,class_name

For example:
/data/imgs/img_001.jpg,837,346,981,456,cow
/data/imgs/img_002.jpg,215,312,279,391,cat

look https://github.com/yhenon/keras-frcnn for detail.
'''
import xml.etree.ElementTree as ET
import os

root='/media/sdb/ISCAS_Dataset/crab/TFFRCNN'
sets = ['3c']
subdirs = ['Annotations', 'JPEGImages']
# github https://github.com/CharlesShang/TFFRCNN
saveto = 'iscas_3c.txt'

write_file=open(saveto,'w')
# maybe change all picture to jpg
img_formats=['jpg','JPG','png','PNG','jpeg','JPEG']
img_target_format='jpg'

i = 1
for set in sets:
    dir = os.path.join(root, set, subdirs[0])
    for f in os.listdir(dir):
        if f.find('xml') != -1:
            if i % 100 == 99:
                print(i,'processing file',f)
            ann_file = os.path.join(dir, f)

            for fmt in img_formats:
                img_file = ann_file.replace(subdirs[0], subdirs[1])
                img_file = img_file.replace('xml', fmt)
                suffix=fmt
                if os.path.exists(img_file):
                    break
            if not os.path.exists(img_file):
                print('warning cannot find image',img_file)
                continue

            tree = ET.parse(ann_file)
            objs = tree.findall('object')
            for obj in objs:
                name = obj.find('name')
                bndbox=obj.find('bndbox')
                x1=bndbox.find('xmin').text
                y1=bndbox.find('ymin').text
                x2=bndbox.find('xmax').text
                y2=bndbox.find('ymax').text
                if name.text.find('carapace') !=-1:
                    write_line=img_file+','+x1+','+y1+','+x2+','+y2+','+'carapace'
                    write_file.write(write_line+'\n')
                elif name.text.find('crab') !=-1:
                    write_line=img_file+','+x1+','+y1+','+x2+','+y2+','+'crab'
                    write_file.write(write_line+'\n')
                elif name.text.find('snail') !=-1:
                    write_line=img_file+','+x1+','+y1+','+x2+','+y2+','+'snail'
                    write_file.write(write_line+'\n')
                else:
                    print('unknow name %s' % name.text)
            
            i = i + 1
write_file.close()
print('total image is ',i-1)
