import cv2
import numpy as np
import serial

ramp_frames = 10
perimeters=[]
threshVal=70
kernel = np.ones((3,3),np.uint8)
#img=cv2.imread("test0.png",1)
cam = cv2.VideoCapture(0)
cam.set(3, 800)
cam.set(4, 600)

def get_image():
 # read is the easiest way to get a full image out of a VideoCapture object.
 retval, im = cam.read()
 return im

for i in range(ramp_frames):
 temp = get_image()

img = get_image()
cam.release()

img_height,img_width=img.shape[:2]
grey_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur_img = cv2.bilateralFilter(grey_img,40,75,75)
_,thresh_img = cv2.threshold(grey_img,threshVal,255,cv2.THRESH_BINARY_INV)
opening = cv2.morphologyEx(thresh_img, cv2.MORPH_OPEN, kernel)

cv2.imshow("grey_img",img)
cv2.imshow("opening",opening)
cv2.waitKey(0)
cv2.destroyAllWindows()
