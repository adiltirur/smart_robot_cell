import cv2
import numpy as np
import serial
import pyads
import time


ramp_frames = 30
perimeters=[]
threshVal=75
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
        
#orgImg=img.copy()
#cv2.imshow("orgimg",orgImg)

#Filters
img_height,img_width=img.shape[:2]
grey_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur_img = cv2.bilateralFilter(grey_img,10,75,75)
_,thresh_img = cv2.threshold(grey_img,threshVal,255,cv2.THRESH_BINARY_INV)
black_img = np.zeros((img_height, img_width))

opening = cv2.morphologyEx(thresh_img, cv2.MORPH_OPEN, kernel)
_,contours, hierarchy = cv2.findContours(opening.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

#cv2.drawContours(black_img,contours,-1,(255,255,255), 1)

#find the outer contour
for i in contours:
    perimeter = cv2.arcLength(i,True)
    perimeters.append(perimeter)
    perimeters.sort()

cnt=contours[len(perimeters)-1]
cv2.drawContours(black_img,[cnt],0,(255,255,255), 1)

#bounding box
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
cv2.drawContours(black_img,[box],0,(255,255,255),1)

angle=int(rect[2])
print("Angle of orientation: ", angle)
x=str(angle*-1)
        
cv2.imshow("thresh",thresh_img)
cv2.imshow("black_img",black_img)
        
cam.release()        
cv2.waitKey(0)
cv2.destroyAllWindows()
print("Exit..")
