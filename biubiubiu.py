#! /usr/bin/env python
# _*_ coding: utf-8 _*_

import os, sys
from PIL import Image

def strchr(sStr1,sStr2):
    a = 0
    try:
        nPos = sStr1.index(sStr2)
        a = nPos
    except:    
        a = -1
    return a


def main():
    scale = (450,400)
    for a in sys.argv:
        if a != sys.argv[0]:
            if isinstance(a,tuple):
                scale = a            
    imageList = os.listdir('./image')
    for index,image in enumerate(imageList):
        if strchr(image,'.jpg') < 0:
            pass
        elif strchr(image,'.pbg') < 0:
            pass
        else:
            str = './image/%s' % image
            im = Image.open(str)
            im.thumbnail(scale)
            im.save(image,'JPEG') 
    print '图片缩放完成！！'

if __name__ == '__main__':
    main()

