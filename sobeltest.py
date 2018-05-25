# -*- coding: utf-8 -*-

import numpy as np
import cv2
import matplotlib.pyplot as plt

# def and_demo(m1, m2):    #与运算  每个像素点每个通道的值按位与
#     andarr = [[0 for col in range(len(m1[0]))] for row in range(len(m1))]
#     for i in range(0,len(m1)):
#         for j in range(0,len(m1[0])):
#             andarr[i][j] = int(m1[i][j]) & int(m2[i][j])
#     return andarr
from PIL import Image

def and_demo(m1, m2):    #与运算  每个像素点每个通道的值按位与
    dst = cv2.bitwise_and(m1, m2)
    # cv2.imshow("and_demo", dst)
    # cv2.waitKey(0)
    return dst

def or_demo(m1, m2):     #或运算   每个像素点每个通道的值按位或
    dst = cv2.bitwise_or(m1, m2)
    cv2.imshow("or_demo", dst)
def not_demo(m1):     #非运算   每个像素点每个通道的值按位取反
    dst = cv2.bitwise_not(m1)
    cv2.imshow("not_demo", dst)


img = cv2.imread('/home/wangbenkang/桌面/test1.jpg')

X1 = 1084
Y1 = 1571

X2 = 1167
Y2 = 1666

W = abs(X1-X2)
H = abs(Y1-Y2)

img_part = img[Y1:Y1 + H, X1:X1 + W]

img_part_gray = cv2.cvtColor(img_part, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_part_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)


sobelx=cv2.Sobel(thresh,cv2.CV_64F,1,0,ksize=3)
sobely=cv2.Sobel(thresh,cv2.CV_64F,0,1,ksize=3)

# image, contourlist, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
anddst = and_demo(sobelx,sobely)

# for contour in contourlist:
#     for i in contour:
#         for j in contour[0]:
#             print(i,j)
    # for i in range(0, len(anddst)):
    #     for j in range(0,len(anddst[0])):
image = Image.fromarray(anddst)
array = np.array(anddst.astype(np.uint8))
cv2.imshow('imge',array)
# im = array.convert("CV_8UC1")

# kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(10, 10))
# opened = cv2.morphologyEx(array, cv2.MORPH_OPEN, kernel)
# closed = cv2.morphologyEx(array, cv2.MORPH_CLOSE, kernel)
# cv2.imshow("Close",closed)

image, contourlist, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)


# 生成纯色图像
background = img_part.copy()
background.fill(255)
# imag = cv2.drawContours(background,contourlist,-1,(55,255,155),1)

# for i in range(len(contourlist) - 1):
#     imag = cv2.drawContours(background, contourlist, i, (0, 0, 0), 1)
#     sobelconx = cv2.Sobel(background, cv2.CV_64F, 1, 0, ksize=3)
#     sobelcony = cv2.Sobel(background, cv2.CV_64F, 0, 1, ksize=3)
#     anddst = and_demo(sobelx,sobely)


imag = cv2.drawContours(background, contourlist, 3, (0, 0, 0), 1)
background_gray = cv2.cvtColor(imag, cv2.COLOR_BGR2GRAY)

ret, binbackground = cv2.threshold(img_part_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

sobelconx = cv2.Sobel(binbackground, cv2.CV_64F, 1, 0, ksize=3)
sobelcony = cv2.Sobel(binbackground, cv2.CV_64F, 0, 1, ksize=3)

condst = and_demo(sobelconx , sobelcony)

sobel_cont_arr = Image.fromarray(condst)

sobel_cont_image = np.array(condst.astype(np.uint8))

cv2.imshow('sobel_cont_image',sobel_cont_image)
cv2.waitKey(0)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5, 5))
opened = cv2.morphologyEx(sobel_cont_image, cv2.MORPH_OPEN, kernel)
cv2.imshow("opened",opened)
cv2.waitKey(0)

nonzero=np.nonzero(condst)
print(nonzero)


cv2.imshow('cont',imag)
cv2.waitKey(0)


plt.subplot(3,1,1)
plt.imshow(sobelx,cmap='gray')
plt.title('X'),plt.xticks([1,2]),plt.yticks([3,4])
plt.subplot(3,1,2)
plt.imshow(condst,cmap='gray')
plt.title('Y'),plt.xticks([]),plt.yticks([])

plt.subplot(3,1,3)
plt.imshow(anddst,cmap='gray')
plt.title('Y'),plt.xticks([]),plt.yticks([])



# image, contourlist, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

plt.show()
