# -*- coding: utf-8 -*-
# resize picture into weixin emotion size
import cv2
import os,sys


def KeepRatioResize(input,dstSize):
    # dstSize=(width,height)
    height,width,c=input.shape
    h = dstSize[0] * (height/(float)(width))
    w = dstSize[1] * (width/(float)(height))
    if h >= dstSize[1]:
        s=((int)(w),dstSize[1])
    else:
        s=(dstSize[0],(int)(h))

    return cv2.resize(input,s)

def CreateWeiXinEmotion(inputdir,outputdir):
    emotion_size=(400,400)
    image_suffix=('.png','.jpg','.bmp','.jpeg')

    if not os.path.exists(inputdir):
        print('cannot find inputdir %s'%inputdir)
        sys.exit(-1)

    if not os.path.exists(outputdir):
        os.mkdir(outputdir)

    for f in os.listdir(inputdir):
        #print('find file %s'%f)
        if os.path.isfile(os.path.join(inputdir,f)) and f.lower().endswith(image_suffix):
            print('process image %s'%f);
            image=cv2.imread(os.path.join(inputdir,f))
            if not image is None:
                image_emotion=KeepRatioResize(image,emotion_size)
                cv2.imwrite(os.path.join(outputdir,f),image_emotion)
            else:
                print('cannot read image %s'%f)