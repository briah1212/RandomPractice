import cv2 
import numpy as np
import sys

image = "C:/Users/brian/Code/testing/first/red_cap.jpg"
img = cv2.imread(image)
output = img.copy()

#display
width = 360
height = 480
display = "Display_Window"


def detect(self):

    img = self

    img = cv2.resize(img, (width,height))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 150,  param1=100, param2=30, minRadius=30, maxRadius=70)

    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        center = (i[0], i[1])
        # circle center
        cv2.circle(img, center, 1, (0, 100, 100), 3)
        # circle outline
        radius = i[2]
        cv2.circle(img, center, radius, (255, 0, 255), 3)

    cv2.imshow(display , img)
    k = cv2.waitKey(0)

