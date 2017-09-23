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
    os.makedirs(abs_output_dir)
    i = 1
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
                    x1 = bndbox.find('xmin').text
                    y1 = bndbox.find('ymin').text
                    x2 = bndbox.find('xmax').text
                    y2 = bndbox.find('ymax').text

                    if name not in namelist:
                        namelist.append(name)
                        os.mkdir(os.path.join(abs_output_dir,name))

                    save_image_filename=os.path.join(abs_output_dir,name,str(i)+'.'+img_target_format)
                    full_image=cv2.imread(img_file)
                    cls_image=full_image[x1:x2,y1:y2]
                    cv2.imwrite(save_image_filename,cls_image)
                i=i+1

                if i>3:
                    break

if __name__ == '__main__':
    root = '/media/sdb/ISCAS_Dataset/crab/TFFRCNN'
    sets = ['3c']
    det2cls(root,sets)