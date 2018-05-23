#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import numpy as np
import cv2
# 找到圆形边缘（找到边缘数最多的边缘）
def findeClipseContours(contours):
    contourslist = []
    for i in range(len(contours)-1):
        contourslist.append(len(contours[i]))
    # print( contourslist.index(max(contourslist)))
    return contourslist.index(max(contourslist))

#img = cv2.imread('/Users/wangbenkang/Desktop/1024.jpg',0)
# ret,thresh = cv2.threshold(img,127,255,0)
# image,contours,hierarchy=cv2.findContours(thresh,1,2)
# cnt=contours[0]
# M=cv2.moments(cnt)
# print(M)

img = cv2.imread('/Users/wangbenkang/Desktop/test.jpg')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

part = imgray[0: 100, 50: 100]
cv2.imshow('center point', part)
#找出图片中的轮廓
ret,thresh = cv2.threshold(imgray,127,255,0)
image ,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_TC89_L1)
#绘制独立轮廓，如第四个轮廓
#imag = cv2.drawContour(img,contours,-1,(0,255,0),3)
#但是大多数时候，下面方法更有用
# imag = cv2.drawContours(img,contours,findeClipseContours(contours),(0,255,0),3)
# findeClipseContours(contours)
# 椭圆拟合
cnt = contours[findeClipseContours(contours)]
ellipse = cv2.fitEllipse(cnt)
eclipseimg = cv2.ellipse(img,ellipse,(55,255,155),2)

# 画出圆心（拟合出的圆心的亚像素级的，画出圆心需像素级，所以需要一次整型转换！）
centerpoint = (int(ellipse[0][0]),int(ellipse[0][1]))
print(centerpoint)
eclipsecenter = cv2.circle(img, centerpoint, 2, (0, 0, 255),-1)

# 文字显示圆心坐标
font = cv2.FONT_HERSHEY_SIMPLEX
text = 'center:' + str(ellipse[0])
cv2.putText(img, text, centerpoint, font,0.5, (255, 255, 0), 1, lineType=cv2.LINE_AA)

while(1):
    # cv2.imshow('img',img)
    # cv2.imshow('imgray',imgray)
    # cv2.imshow('image',image)
    # cv2.imshow('imag',imag)
    cv2.imshow('eclipse',eclipseimg)
    cv2.imshow('center point', eclipsecenter)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()

