# -*- coding: utf-8 -*-
"""
convert classification dataset to detection dataset
input: image, background
output: image+background,xml annotation
"""

import cv2
import os,sys
import random,numpy

from imgaug import augmenters as iaa

sys.path.append('/home/yzbx/git/yzbxLib/gnu')
from pascal_voc_io import PascalVocWriter

class classify2detect:
    def process(image,background,objectName,xml,jpeg):
        """

        :param image: input image filename
        :param background: background filename
        :param objectName: name of object
        :param xml: xml filename
        :param jpeg: jpeg image filename
        :return: write annotation to xml
        """

        if type(image) == str:
            cvin=cv2.imread(image)
            if cvin is None:
                print('cannot open image %s' % image)
                sys.exit(-1)
        elif type(image) == numpy.ndarray:
            cvin=image
        else:
            print('invalided image')
            sys.exit(-1)

        if type(background) == str:
            cvbg=cv2.imread(background)
            if cvbg is None :
                print('cannot open background %s'%background)
                sys.exit(-1)
        elif type(background) == numpy.ndarray:
            cvbg=background
        else:
            print('invalided background')
            sys.exit(-1)

        assert(len(cvin.shape)==3)
        assert(len(cvbg.shape)==3)

        cvin=classify2detect.resize(cvin,cvbg)

        shapein=cvin.shape
        shapebg=cvbg.shape


        shift=[0,0]
        shift[0]=shapebg[0]-shapein[0]
        shift[1]=shapebg[1]-shapein[1]

        top=random.randint(1,shift[0]-1)
        left=random.randint(1,shift[1]-1)
        right=left+shapein[1]
        bottom=top+shapein[0]

        cvjpeg=classify2detect.merge(cvin,cvbg,[top,left])
        cv2.imwrite(jpeg,cvjpeg)

        xmlwriter=PascalVocWriter(foldername='./', filename=jpeg, imgSize=shapebg)
        xmlwriter.addBndBox(xmin=left, ymin=top, xmax=right, ymax=bottom, name=objectName, difficult=0)
        xmlwriter.save(targetFile=xml)

    def resize(cvin,cvbg):
        """
        make cvin small than cvbg
        :param cvin: opencv image
        :param cvbg: opencv image
        :return: opencv image
        """

        while True:
            shapein = cvin.shape
            shapebg = cvbg.shape
            print('shapein',shapein)
            print('shapebg',shapebg)
            if shapein[0]+20 > shapebg[0] or shapein[1]+20 > shapebg[1]:
                cvin=cv2.resize(cvin,dsize=(0,0),fx=0.5,fy=0.5)
            else:
                break

        return cvin

    def merge(smallImage,largeImage,shift):
        """
        merge small image on large image
        :param smallImage:
        :param largeImage:
        :return: merged image
        """

        s_img=smallImage
        l_img=largeImage
        y_offset=shift[0]
        x_offset=shift[1]
        for c in range(0, 3):
            l_img[y_offset:y_offset + s_img.shape[0], x_offset:x_offset + s_img.shape[1], c] = s_img[:, :, c]

        return l_img


class RandomDataset:
    def __init__(self,imageFolder,backgroundFolder):
        self.imageFolder=imageFolder
        self.backgroundFolder=backgroundFolder
        imgfmt=('jpg','JPG','png','PNG','bmp','BMP','jpeg','JPEG','ppm')

        filelist=[f for f in os.listdir(imageFolder) if os.path.isfile(os.path.join(imageFolder, f))]
        self.imagelist=[f for f in filelist if f.endswith(imgfmt)]

        filelist=[f for f in os.listdir(backgroundFolder) if os.path.isfile(os.path.join(backgroundFolder, f))]
        self.backgroundlist=[f for f in filelist if f.endswith(imgfmt)]

        self.seq = iaa.Sequential([
            #iaa.Crop(px=(0, 16)), # crop images from each side by 0 to 16px (randomly chosen)
            #iaa.Fliplr(0.5), # horizontally flip 50% of the images
            iaa.GaussianBlur(sigma=(0.1, 0.5)), # blur images with a sigma of 0 to 3.0
            iaa.Multiply(V=(0.5, 1.5)),
            iaa.Dropout(p=(0.01,0.1)),
            iaa.Affine(scale=(0.8, 2))
        ])

    def process(self, batch=16, objectName='unknow',times=4):
        gnum=0
        lnum=0

        maxnum=len(self.imagelist)*times
        while gnum < maxnum :

            images=[]
            for lnum in range(0, batch):
                if gnum + lnum < maxnum:
                    images.append(cv2.imread(os.path.join(self.imageFolder, self.imagelist[gnum+lnum])))
                else:
                    break

            images_aug=[]
            for i in range(0,times):
                images_aug_i = self.seq.augment_images(images)
                images_aug.extend(images_aug_i)

            for i,image in enumerate(images_aug):
                bgnum=random.randint(0,len(self.backgroundlist)-1)
                bgfile=os.path.join(self.backgroundFolder,self.backgroundlist[bgnum])
                bgimg=cv2.imread(bgfile)

                xml='%d.xml'%(gnum+i+1)
                jpeg='%d.jpg'%(gnum+i+1)

                print('%d/%d: save image to %s, save xml to %s'%(gnum+i+1,maxnum,jpeg,xml))
                classify2detect.process(image=image,
                                     background=bgimg,
                                     objectName=objectName,
                                     xml=xml,
                                     jpeg=jpeg)

            gnum = gnum + len(images_aug)

if __name__ == '__main__':
    ranset=RandomDataset(imageFolder='/home/yzbx/Pictures/dataset/pedestrians128x64',
                         backgroundFolder='/home/yzbx/Pictures/dataset/Pasadena-Houses')
    ranset.process(batch=16,objectName='person')
