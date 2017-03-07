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
    finish = False
    hasImage = False
    for index,image in enumerate(imageList):
        if strchr(image,'.jpg') >= 0:
            hasImage = True
            pass
        if strchr(image,'.png') >= 0:
            hasImage = True
            pass
        if hasImage:
            finish = True
            str = './image/%s' % image
            im = Image.open(str)
            im.thumbnail(scale)
            im.save(image,'JPEG')
    if finish:
        print '图片处理完成'
    else:
        print '未发现图片'   
if __name__ == '__main__':
    main()

