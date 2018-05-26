import cv2
import numpy as np

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

    ret, thresh = cv2.threshold(img_part_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # find ellipse by sobel in XY direction
    sobelxy = cv2.Sobel(thresh, cv2.CV_64F, 1, 1, ksize=3)

    # DILATE sobelxy  image
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    img_dilate = cv2.morphologyEx(sobelxy, cv2.MORPH_DILATE, kernel)

    image, contourlist, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)