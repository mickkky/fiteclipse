import cv2
import numpy as np
def drawcenterpoint(img , X1 , Y1 , X2 , Y2 ,image_name):
    W = abs(X1 - X2)
    H = abs(Y1 - Y2)
    img_part = img[Y1:Y1 + H, X1:X1 + W]
    img_part_gray = cv2.cvtColor(img_part, cv2.COLOR_BGR2GRAY)

    # find circles by hough transform
    houghcircles = cv2.HoughCircles(img_part_gray, cv2.HOUGH_GRADIENT, 1, 20, param1=100, param2=20, minRadius=0, maxRadius=0)

    # Can not find circle in this box.
    if len(houghcircles) == 0:
        print('Can not find circle in this box.')
    # if find c
    else:
        ret, thresh = cv2.threshold(img_part_gray, 127, 255, 0)
        image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

        circlescenter_list = []
        ellipse_list = []

        # find the best ellipse during all ellipses that finded by findContours
        for i in range(len(contours) - 1):

            # if number of contours is less than 5, it's means that is not a ellipse contours, and skip it

            if ( len( contours[i] ) < 5 ):
                continue

            cnt = contours[i]
            ellipse = cv2.fitEllipse(cnt)
            distance = pow((ellipse[0][0] - houghcircles[0, 0][0]), 2) + pow((ellipse[0][1] - houghcircles[0, 0][1]), 2)
            circlescenter_list.append(distance)
            ellipse_list.append(ellipse)

        # choose ellipse that have min distance between ellipse center and hough circle center
        Index = circlescenter_list.index(min(circlescenter_list))
        eclipse_img_inpart = cv2.ellipse(img_part, ellipse_list[Index], (0, 255, 155), 1)

        # coordinate of centerpoint float2int
        center_XY = (X1 + int(ellipse_list[Index][0][0]), Y1 + int(ellipse_list[Index][0][1]))

        print(center_XY)
        eclipsecenter = cv2.circle(img, center_XY, 1, (0, 0, 255),-1)

        cv2.imwrite(image_name, img, [int(cv2.IMWRITE_PNG_COMPRESSION),100])

def drawcenterpoint(img , dets ,image_name,thresh=0.5):

    inds = np.where(dets[:, -1] >= thresh)[0]
    if len(inds) == 0:
        return

    for i in inds:
        bbox = dets[i, :4]

        X1 = bbox[0]
        Y1 = bbox[1]

        X2 = bbox[2]
        Y2 = bbox[3]

        W = abs(X1 - X2)
        H = abs(Y1 - Y2)
        img_part = img[Y1:Y1 + H, X1:X1 + W]
        img_part_gray = cv2.cvtColor(img_part, cv2.COLOR_BGR2GRAY)

        # find circles by hough transform
        houghcircles = cv2.HoughCircles(img_part_gray, cv2.HOUGH_GRADIENT, 1, 20, param1=100, param2=20, minRadius=0, maxRadius=0)

        # Can not find circle in this box.
        if len(houghcircles) == 0:
            print('Can not find circle in this box.')
        # if find c
        else:
            ret, thresh = cv2.threshold(img_part_gray, 127, 255, 0)
            image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

            circlescenter_list = []
            ellipse_list = []

            # find the best ellipse during all ellipses that finded by findContours
            for i in range(len(contours) - 1):

                # if number of contours is less than 5, it's means that is not a ellipse contours, and skip it

                if ( len( contours[i] ) < 5 ):
                    continue

                cnt = contours[i]
                ellipse = cv2.fitEllipse(cnt)
                distance = pow((ellipse[0][0] - houghcircles[0, 0][0]), 2) + pow((ellipse[0][1] - houghcircles[0, 0][1]), 2)
                circlescenter_list.append(distance)
                ellipse_list.append(ellipse)

            # choose ellipse that have min distance between ellipse center and hough circle center
            Index = circlescenter_list.index(min(circlescenter_list))
            eclipse_img_inpart = cv2.ellipse(img_part, ellipse_list[Index], (0, 255, 155), 1)

            # coordinate of centerpoint float2int
            center_XY = (X1 + int(ellipse_list[Index][0][0]), Y1 + int(ellipse_list[Index][0][1]))

            print(center_XY)
            eclipsecenter = cv2.circle(img, center_XY, 1, (0, 0, 255),-1)

            cv2.imwrite(image_name, img, [int(cv2.IMWRITE_PNG_COMPRESSION),100])
            print('{} have been writed.'.format(image_name))


def drawcenterpoint(img , X1 , Y1 , X2 , Y2 ,image_name):
    W = abs(X1 - X2)
    H = abs(Y1 - Y2)
    img_part = img[Y1:Y1 + H, X1:X1 + W]
    img_part_gray = cv2.cvtColor(img_part, cv2.COLOR_BGR2GRAY)


    ret, thresh = cv2.threshold(img_part_gray, 127, 255, 0)
    image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    for index in hierarchy[:][0]:
        imag = cv2.drawContours(img_part_gray, contours, 1, (0, 255, 0), 3)
        cv2.imshow('contours',imag)
        cv2.waitKey(0)
    circlescenter_list = []
    ellipse_list = []

    # find the best ellipse during all ellipses that finded by findContours
    # for i in range(len(contours) - 1):
    #
    #     # if number of contours is less than 5, it's means that is not a ellipse contours, and skip it
    #
    #     if ( len( contours[i] ) < 5 ):
    #         continue
    #
    #     cnt = contours[i]
    #     ellipse = cv2.fitEllipse(cnt)
    #     distance = pow((ellipse[0][0] - houghcircles[0, 0][0]), 2) + pow((ellipse[0][1] - houghcircles[0, 0][1]), 2)
    #     circlescenter_list.append(distance)
    #     ellipse_list.append(ellipse)

    # choose ellipse that have min distance between ellipse center and hough circle center
    Index = circlescenter_list.index(min(circlescenter_list))
    eclipse_img_inpart = cv2.ellipse(img_part, ellipse_list[Index], (0, 255, 155), 1)

    # coordinate of centerpoint float2int
    center_XY = (X1 + int(ellipse_list[Index][0][0]), Y1 + int(ellipse_list[Index][0][1]))

    print(center_XY)
    eclipsecenter = cv2.circle(img, center_XY, 1, (0, 0, 255),-1)

    cv2.imwrite(image_name, img, [int(cv2.IMWRITE_PNG_COMPRESSION),100])