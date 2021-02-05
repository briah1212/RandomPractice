import cv2 
import numpy as np
import sys
import detect_ball
import contour

image = "C:/Users/brian/Code/testing/first/stop_sign.jpg"

#display
width = 900
height = 480
display = "Display_Window"

img = cv2.imread(image)

if img is None:
    sys.exit("Could not read the image.")

img = cv2.resize(img, (width,height)) #make img smaller
img = cv2.blur(img, (1,1)) #blur a little

#d_img = img.copy()

#color mask
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
dark_red = np.array([0, 50, 132])
light_red = np.array([179, 255,255])
mask_hsv = cv2.inRange(hsv, dark_red, light_red)
img = cv2.bitwise_and(img, img, mask=mask_hsv)

#erode and dialate cuz why not
img = cv2.erode(img, None, iterations=2)
img = cv2.dilate(img, None, iterations=1)

#rgb mask (doesnt need?)
#dark = np.array([50,50,50])
#light = np.array([255,255,255])
#mask_rgb = cv2.inRange(img, dark, light)
#img = cv2.bitwise_and(img,img, mask=mask_rgb)

while True:
    cv2.imshow(display, img)
    k = cv2.waitKey(0)

    #if k == ord('d'):
        #detect_ball.detect(d_img)

    if k == ord('c'):
        contour.contours(img)

    if k == ord('f'):
        cv2.imshow(display, img)

    if k == ord('q'):
        cv2.destroyAllWindows()
        break

    if k == ord("s"):
        cv2.imwrite("new red_cap.jpg", img)

