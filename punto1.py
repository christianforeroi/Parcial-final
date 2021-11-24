import cv2
import os
import sys
import numpy as np
""" Color filtering based on Hue histogram peak (use soccer_game.png as example)

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
    n_white_pix = np.sum(mask == 255)
    n_black_pix = np.sum(mask == 0)
    print("Porcentaje de pixeles de cesped: {}".format(n_white_pix/(n_white_pix+n_black_pix)))

    cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Image", 1280, 720)
    cv2.imshow("Image", mask)
    cv2.waitKey(0)
