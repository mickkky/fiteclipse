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

protoimg = cv2.imread('/home/wangbenkang/桌面/test1.jpg')

X1 = 1111
Y1 = 1593

X2 = 1208
Y2 = 1700

W = abs(X1-X2)
H = abs(Y1-Y2)

img = protoimg[Y1:Y1+H, X1:X1+W]
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


houghcircles = cv2.HoughCircles(imgray, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
# for i in houghcircles[0,:]:
#     # draw the outer circle
#     cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
#     # draw the center of the circle
#     cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

#找出图片中的轮廓
ret,thresh = cv2.threshold(imgray,127,255,0)
image , contours,hierarchy = cv2.findContours(thresh,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
#绘制独立轮廓，如第四个轮廓
#imag = cv2.drawContour(img,contours,-1,(0,255,0),3)
#但是大多数时候，下面方法更有用
# imag = cv2.drawContours(img,contours,1,(0,255,0),3)
# findeClipseContours(contours)
# 椭圆拟合
circlescenter_list = []
ellipse_list = []
for i in range(len(contours) - 1):

    if(len(contours[i])<6):
        continue

    cnt = contours[i]
    ellipse = cv2.fitEllipse(cnt)
    distance = pow((ellipse[0][0]-houghcircles[0,0][0]),2)+pow((ellipse[0][1]-houghcircles[0,0][1]),2)
    circlescenter_list.append(distance)
    ellipse_list.append(ellipse)

Index = circlescenter_list.index(min(circlescenter_list))  # 圆心距最小值
eclipseimg = cv2.ellipse(img, ellipse_list[Index], (55, 255, 155), 2)

# cnt = contours[3]
# ellipse = cv2.fitEllipse(cnt)
# eclipseimg = cv2.ellipse(img,ellipse,(55,255,155),2)

# 画出圆心（拟合出的圆心的亚像素级的，画出圆心需像素级，所以需要一次整型转换！）
centerpoint = (X1+int(ellipse_list[Index][0][0]),Y1+int(ellipse_list[Index][0][1]))
print(centerpoint)
eclipsecenter = cv2.circle(protoimg, centerpoint, 2, (0, 0, 255),-1)

# 文字显示圆心坐标
font = cv2.FONT_HERSHEY_SIMPLEX
text = 'center:' + str(ellipse_list[Index][0])
cv2.putText(protoimg, text, centerpoint, font,0.5, (255, 255, 0), 1, lineType=cv2.LINE_AA)

while(1):
    # cv2.imshow('img',img)
    # cv2.imshow('imgray',imgray)
    # cv2.imshow('image',image)
    cv2.namedWindow('protoimg',cv2.WINDOW_NORMAL)
    cv2.imshow('protoimg', protoimg)

    cv2.waitKey(0)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()
