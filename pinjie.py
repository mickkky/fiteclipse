# -*- coding: utf-8 -*-
import os
import cv2
import numpy
from PIL import Image

# UNIT_SIZE = 229 # the size of image
def pinjie(images,row,col,imagname):

    w, h = images[0].size
    target = Image.new('RGB', (w*col, h*row))   # result is 2*2
    leftone = 0
    lefttwo = 0
    rightone = w
    righttwo = w
    for i in range(len(images)):
        if(i==0 or i==1):
            target.paste(images[i], (leftone, 0, rightone, h))
            leftone += w #第一行左上角右移
            rightone += w #右下角右移
        else:
            target.paste(images[i], (lefttwo, h, righttwo, h*row))
            lefttwo += w #第二行左上角右移
            righttwo += w #右下角右移
    quality_value = 100
    target.save(imagname+'.jpg', quality = quality_value)


def splitimage(img, rownum, colnum, dstpath):
    # img = Image.open(src)
    w, h = img.size
    if rownum <= h and colnum <= w:
        print('Original image info: %sx%s, %s, %s' % (w, h, img.format, img.mode))
        print('开始处理图片切割, 请稍候...')

        s = os.path.split(src)
        if dstpath == '':
            dstpath = s[0]
        fn = s[1].split('.')
        basename = fn[0]
        ext = 'png'

        num = 0
        rowheight = h // rownum
        colwidth = w // colnum
        imagepieces = []
        imagelist = []
        for r in range(rownum):
            for c in range(colnum):
                box = (c * colwidth, r * rowheight, (c + 1) * colwidth, (r + 1) * rowheight)
                # a=img.crop(box)
                imagelist.append(img.crop(box))

                imagepiece = cv2.cvtColor(numpy.asarray(img.crop(box)), cv2.COLOR_RGB2GRAY)
                a = imagepiece.shape
                imagepieces.append(imagepiece)
                # cv2.imshow('sss',imagepiece)
                # cv2.waitKey(0)

                img.crop(box).save(os.path.join(dstpath, basename + '_' + str(num) + '.' + ext), ext)
                num = num + 1

        print('图片切割完毕，共生成 %s 张小图片。' % num)
        return imagelist
    else:
        print('不合法的行列切割参数！')


row = 2
col = 2
src = 'test1.jpg'
dstpath = ''
img = Image.open(src)
imalist = splitimage(img, row, col, dstpath)


imagname ='test'
pinjie(imalist,2,2,imagname)

# imalist = []