# -*- coding: utf-8 -*-

import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image


# 输入灰度图，返回hash
def getHash(threshimage):
    avreage = 0
    hash = []
    for i in range(threshimage.shape[0]):
        for j in range(threshimage.shape[1]):
            if threshimage[i, j] != avreage:
                hash.append(1)
            else:
                hash.append(0)
    return hash


# # 计算汉明距离
# def Hamming_distance(hash1, hash2):
#     num = 0
#     for index in range(len(hash1)):
#         if hash1[index] != hash2[index]:
#             num += 1
#     return num

    # 计算汉明距离
def Hamming_distance(threshimg1, threshimg2):
    num = 0
    hash1 = getHash(threshimg1)
    hash2 = getHash(threshimg2)

    for index in range(threshimg2.shape[0]+1,len(hash1)-threshimg2.shape[0]-1):
        # up and down
        if hash1[index] != hash2[index-1]:
            num += 1
        elif hash1[index] != hash2[index+1]:
            num += 1

        # right and left
        elif hash1[index] != hash2[index - threshimg2.shape[1]]:
            num += 1
        elif hash1[index] != hash2[index + threshimg2.shape[1]]:
            num += 1

        elif hash1[index] != hash2[index - threshimg2.shape[1] + 1]:
            num += 1
        elif hash1[index] != hash2[index - threshimg2.shape[1] - 1]:
            num += 1

        elif hash1[index] != hash2[index + threshimg2.shape[1] + 1]:
            num += 1
        elif hash1[index] != hash2[index + threshimg2.shape[1] - 1]:
            num += 1

        elif hash1[index] != hash2[index]:
            num += 1
    return num

# def Remove_edge(img,contourlist):
#     for contour in contourlist:
#         for col in range(contour[0]):
#             if
#             for row in range(contour[1]):






img = cv2.imread('/Users/wangbenkang/Desktop/test1.jpg')

X1 = 1084
Y1 = 1571

X2 = 1160
Y2 = 1688

W = abs(X1-X2)
H = abs(Y1-Y2)

img_part = img[Y1:Y1 + H, X1:X1 + W]

img_part_gray = cv2.cvtColor(img_part, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_part_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# threshblur = cv2.blur(thresh,(3,3))
sobelxy=cv2.Sobel(thresh,cv2.CV_64F,1,1,ksize=1)

cv2.imshow('imge',sobelxy)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5, 5))
DILATE = cv2.morphologyEx(sobelxy, cv2.MORPH_DILATE, kernel)

cv2.imshow("DILATE",DILATE)
# cv2.imshow("thresh",thresh)

image, contourlist, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# a =contourlist.remove(contourlist[0][0][0])

background = img_part_gray.copy()
hamminglist = []
contlen = []
lines = []
a = np.array([2,3,4])
for i in range(len(contourlist)):

    background.fill(0)
    contour_in_background = cv2.drawContours(background, contourlist, i, (255,255,255), cv2.FILLED)

    # sobelcnt = cv2.Sobel(contour_in_background, cv2.CV_64F, 1, 1, ksize=1)
    # cv2.imshow("sobelcnt", sobelcnt)
    # cv2.waitKey(0)

    edges = cv2.Canny(contour_in_background, 50, 200)

    lines = cv2.HoughLines(edges, 1, np.pi / 180, 60)
    # print lines[0]
    print(len(contourlist[1]))
    print(type(lines))
    if type(lines) != type(a):
        if len(contourlist[i])> 8:
            contour_in_background = cv2.drawContours(img_part, contourlist, i, (0, 255, 155), 4)
            ellipse = cv2.fitEllipse(contourlist[i])
            eclipse_img_inpart = cv2.ellipse(img_part, ellipse, (0, 255, 155), 2)

            # center_XY = (X1+int(ellipse[0][0]),Y1+int(ellipse[0][1]))
            center_XY = (int(ellipse[0][0]), int(ellipse[0][1]))
            print(center_XY)

            eclipsecenter = cv2.circle(img_part, center_XY, 1, (0, 0, 255), -1)
    # cv2.imshow("img_part", img_part)
    # cv2.waitKey(0)

    # distance = Hamming_distance(DILATE,contour_in_background)
    # hamminglist.append(distance)
    # contlen.append(len(contourlist[i]))

# 生成纯色图像
# ellipseIndex = hamminglist.index(min(hamminglist))

# background = img_part_gray.copy()
background.fill(0)

# contour_in_background = cv2.drawContours(background, contourlist, 4, (255, 255, 255), 1)

# distance = Hamming_distance(contour_in_background,DILATE)
# print distance
ellipsecont= cv2.drawContours(background, contourlist, 1, (255, 255, 255), 1)
cv2.imshow("ellipsecont",ellipsecont)
cv2.imshow("img_part", img_part)
cv2.waitKey(0)

# cv2.waitKey(0)
