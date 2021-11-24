import cv2
import os
import sys
import numpy as np
import math
points = []
import hough

def click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(points)<2:
            points.append((x, y))
            #print(points)
        if len(points)==2:
            cv2.line(image, points[0], points[1], (255,0,0))


if __name__ == '__main__':

    image=cv2.imread("cesped.jpeg")
    cv2.namedWindow("Image")
    cv2.setMouseCallback("Image", click)
    while True:
        cv2.imshow("Image", image)
        key = cv2.waitKey(1) & 0xFF
        if len(points)==2:
            image2=image
            cv2.destroyAllWindows()
            break

    cv2.imshow("imagen2",image2)
    cv2.waitKey(0)
