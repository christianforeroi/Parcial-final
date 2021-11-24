import cv2
import os
import sys
import numpy as np
""" People detection using contours
"""

if __name__ == '__main__':
    image= cv2.imread("cesped.jpeg")

    # Hue histogram
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hist_hue = cv2.calcHist([image_hsv], [0], None, [180], [0, 180])

    # Hue histogram max and location of max
    max_val = hist_hue.max()
    max_pos = int(hist_hue.argmax())

    # Peak mask
    lim_inf = (max_pos - 11, 0, 0)
    lim_sup = (max_pos + 11, 255, 255)
    mask = cv2.inRange(image_hsv, lim_inf, lim_sup)
    mask2=mask

    kernel = np.ones((4, 4), np.uint8)
    mask2 = cv2.morphologyEx(mask2, cv2.MORPH_OPEN, kernel)
    kernel = np.ones((6, 6), np.uint8)
    mask2 = cv2.morphologyEx(mask2, cv2.MORPH_CLOSE, kernel)

    mask_not= cv2.bitwise_not(mask2)
    contador=0
    contours, hierarchy = cv2.findContours(mask_not, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    image_draw = image.copy()
    for idx, cont in enumerate(contours):
        if len(contours[idx]) > 10 and len(contours[idx]) < 200:
            hull = cv2.convexHull(contours[idx])
            M = cv2.moments(contours[idx])
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            area = M['m00']
            if area <3000 and area >200:
                x, y, width, height = cv2.boundingRect(contours[idx])
                cv2.rectangle(image_draw, (x, y), (x + width, y + height), (0, 0, 255), 2)
                contador=contador+1

    print("En la cancha se encuentran : {} jugadores".format(contador))
    cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Image", 1280, 720)
    cv2.imshow("Image", image_draw)
    cv2.waitKey(0)
