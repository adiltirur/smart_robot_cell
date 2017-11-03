import cv2
import numpy as np

perimeters=[]
threshVal=80
img=cv2.imread("Images/as.jpg",1)
img_height,img_width=img.shape[:2]
blur_img = cv2.bilateralFilter(img,100,75,75)
grey_img = cv2.cvtColor(blur_img,cv2.COLOR_BGR2GRAY)
_,thresh_img = cv2.threshold(grey_img,threshVal,255,cv2.THRESH_BINARY)
black_img = np.zeros((img_height, img_width))
black_img2 = thresh_img.copy()


#find the contours in the image
_,contours, hierarchy = cv2.findContours(thresh_img.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)


cv2.drawContours(black_img2, contours, -1, (0,255,0), 3)

_,contours2, hierarchy2 = cv2.findContours(black_img2.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

#find the outer contour
for i in contours2:
	perimeter = cv2.arcLength(i,True)
	perimeters.append(perimeter)
	perimeters.sort()
#cnt2=contours2[len(perimeters)-1]

print (len(contours2))

#find the outer contour
for i in contours:
	perimeter = cv2.arcLength(i,True)
	perimeters.append(perimeter)
	perimeters.sort()

cnt=contours[len(perimeters)-1]

#aproximation
#epsilon = 0.1*cv2.arcLength(cnt,True)
#approx = cv2.approxPolyDP(cnt,epsilon,True)
cv2.drawContours(black_img,[cnt],0,(255,255,255), 1)


#bounding box
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
cv2.drawContours(black_img,[box],0,(255,255,255),2)

#extracting angle of the bounding box
angle=rect[2]
print("Angle of orientation: ", angle)

cv2.imshow("black_img2",black_img2)
#cv2.imshow("blur_img",blur_img)
#cv2.imshow("thresh_img",thresh_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
