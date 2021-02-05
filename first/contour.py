import cv2 
import numpy as np
import sys

image = "C:/Users/brian/Code/testing/first/stop_sign.jpg"

#display
width = 900
height = 480
display = "Display_Window"

img = cv2.imread(image)
img = cv2.resize(img, (width,height)) 
img = cv2.blur(img, (5,5))

def contours(self):
  
    img = self
  
    img2 = img.copy()

    edge_img = cv2.Canny(img, 100, 150)
    contours, _= cv2.findContours(edge_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contour_list = []
    for contour in contours:
        approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
        area = cv2.contourArea(contour)
        if ((len(approx) == 8) & (area > 400) ):
            contour_list.append(contour)

    cv2.drawContours(img2, contour_list,  -1, (255,0,0), 2)
    cv2.imshow('Objects Detected',img2)
    cv2.waitKey(0)

    cv2.imshow('Edge_shown', edge_img)
    cv2.waitKey(0)


'''
def coordinates(contours):
    
    font = cv2.FONT_HERSHEY_COMPLEX
    
    n = contours.approx.ravel() 
    i = 0

    for j in n : 
        if(i % 2 == 0): 
            x = n[i] 
            y = n[i + 1] 

            # String containing the co-ordinates. 
            string = str(x) + " " + str(y)  

            if(i == 0): 
                # text on topmost co-ordinate. 
                cv2.putText(img2, "Arrow tip", (x, y), 
                                font, 0.5, (255, 0, 0))  
            else: 
                # text on remaining co-ordinates. 
                cv2.putText(img2, string, (x, y),  
                            font, 0.5, (0, 255, 0))  
        i = i + 1

    # Showing the final image. 
    cv2.imshow('image2', img2)  
    cv2.waitKey(0)
    '''

