# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt


def getHash(threshimage):
    avreage = 0
    hash = []
    for i in range(threshimage.shape[0]):
        for j in range(threshimage.shape[1]):
            if threshimage[i, j] > avreage:
                hash.append(1)
            else:
                hash.append(0)
    return hash

def Hamming_distance(threshimg1, threshimg2):
    num = 0
    hash1 = getHash(threshimg1)
    hash2 = getHash(threshimg2)

    for index in range(len(hash1)):
        if hash1[index] != hash2[index]:
            num += 1
    return num

def drawcenterpoint(img , X1 , Y1 , X2 , Y2 ,image_name):
    W = abs(X1 - X2)
    H = abs(Y1 - Y2)

    img_part = img[Y1:Y1 + H, X1:X1 + W]
    img_part_gray = cv2.cvtColor(img_part, cv2.COLOR_BGR2GRAY)

    # Binarization
    ret, thresh = cv2.threshold(img_part_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    image, contourlist, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    background = img_part_gray.copy()

    temptype = np.array([2, 3, 4])

    for i in range(len(contourlist)):

        background.fill(0)
        contour_in_background = cv2.drawContours(background, contourlist, i, (255, 255, 255), cv2.FILLED)

        edges = cv2.Canny(contour_in_background, 50, 200)

        lines = cv2.HoughLines(edges, 1, np.pi / 180, 60)

        if type(lines) != type(temptype):
            if len(contourlist[i]) > 20:
                contour_in_background = cv2.drawContours(img_part, contourlist, i, (0, 255, 155), 4)
                ellipse = cv2.fitEllipse(contourlist[i])
                eclipse_img_inpart = cv2.ellipse(img_part, ellipse, (0, 255, 155), 2)

                center_XY = (X1+int(ellipse[0][0]),Y1+int(ellipse[0][1]))
                # center_XY = (int(ellipse[0][0]), int(ellipse[0][1]))
                print(ellipse[0][0],ellipse[0][1])

                eclipsecenter = cv2.circle(img, center_XY, 1, (0, 0, 255), -1)

    ellipsecont = cv2.drawContours(background, contourlist, 1, (255, 255, 255), 1)

    # cv2.imshow("ellipsecont", ellipsecont)
    # cv2.namedWindow('img', cv2.WINDOW_NORMAL)
    # cv2.imshow("img", img)
    # cv2.waitKey(0)

    plt.subplot(1, 1, 1)
    plt.imshow(img, cmap='gray')
    # plt.title('X'), plt.xticks([1, 2]), plt.yticks([3, 4])
    plt.show()

if __name__ == '__main__':

    X1 = 1084
    Y1 = 1571

    X2 = 1200
    Y2 = 1700
    # protoimg = cv2.imread('/home/wangbenkang/桌面/test1.jpg')
    protoimg = cv2.imread('test1.jpg')
    drawcenterpoint(protoimg,X1,Y1,X2,Y2,'1111.jpg')