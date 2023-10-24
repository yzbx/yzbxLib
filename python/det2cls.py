import os
import cv2
import sys
import xml.etree.ElementTree as ET

def det2cls(root,sets,output_dir='classification'):
    subdirs = ['Annotations', 'JPEGImages']
    # maybe change all picture to jpg
    img_formats = ['jpg', 'JPG', 'png', 'PNG', 'jpeg', 'JPEG']
    img_target_format = 'jpg'
    abs_output_dir=os.path.join(root,output_dir)

    if not os.path.exists(abs_output_dir):
        os.makedirs(abs_output_dir)

    # number of xml file
    i = 1
    # number of image file for classfication
    j = 1
    namelist=[]
    for set in sets:
        xml_dir = os.path.join(root, set, subdirs[0])
        for f in os.listdir(xml_dir):
            if f.find('xml') != -1:
                if i % 100 == 99:
                    print(i, 'processing file', f)
                ann_file = os.path.join(xml_dir, f)

                for fmt in img_formats:
                    img_file = ann_file.replace(subdirs[0], subdirs[1])
                    img_file = img_file.replace('xml', fmt)
                    suffix = fmt
                    if os.path.exists(img_file):
                        break
                if not os.path.exists(img_file):
                    print('warning cannot find image', img_file)
                    continue

                tree = ET.parse(ann_file)
                objs = tree.findall('object')
                for obj in objs:
                    name = obj.find('name').text
                    bndbox = obj.find('bndbox')
                    x1 = int(bndbox.find('xmin').text)
                    y1 = int(bndbox.find('ymin').text)
                    x2 = int(bndbox.find('xmax').text)
                    y2 = int(bndbox.find('ymax').text)

                    if name not in namelist:
                        namelist.append(name)
                        name_cls_dir=os.path.join(abs_output_dir,name)
                        if not os.path.exists(name_cls_dir):
                            os.mkdir(name_cls_dir)

                    save_image_filename=os.path.join(abs_output_dir,name,str(j)+'.'+img_target_format)
                    full_image=cv2.imread(img_file)
                    cls_image=full_image[y1:y2,x1:x2]
                    cv2.imwrite(save_image_filename,cls_image)
                    j=j+1

                i=i+1

    print('namelist is ',namelist)

if __name__ == '__main__':
    root = '/media/sdb/ISCAS_Dataset/crab/TFFRCNN'
    sets = ['cls']
    det2cls(root,sets)