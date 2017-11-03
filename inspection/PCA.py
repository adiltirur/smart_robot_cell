import cv2
import numpy as np
import matplotlib.pyplot as plt

perimeters=[]
threshVal=50
img=cv2.imread("Images/Square35.jpg",1)
img_height,img_width=img.shape[:2]
blur_img = cv2.bilateralFilter(img,1,75,75)
grey_img=cv2.cvtColor(blur_img,cv2.COLOR_BGR2GRAY)
_,thresh_img=cv2.threshold(grey_img,threshVal,255,cv2.THRESH_BINARY)
black_img = np.zeros((img_height, img_width))
#contour detection
_,contours, hierarchy = cv2.findContours(thresh_img.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

#find the outer contour
for i in contours:
	perimeter = cv2.arcLength(i,True)
	perimeters.append(perimeter)
	perimeters.sort()

cnt = contours[len(perimeters)-1]
#find the center of the contour
M = cv2.moments(cnt)
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
center=np.array([cx,cy],int)
print (center)
cv2.drawContours(black_img,[cnt],0,(255,255,255),2)
#extract contour points
y, x = np.nonzero(black_img)
x = x - np.mean(x)
y = y - np.mean(y)
coords = np.vstack([x, y])
cov = np.cov(coords)
evals, evecs = np.linalg.eig(cov)
sort_indices = np.argsort(evals)[::-1]
evec1, evec2 = evecs[:, sort_indices]
# Eigenvector with largest eigenvalue
x_v1, y_v1 = evec1  
x_v2, y_v2 = evec2
scale=200
cv2.circle(black_img, (cx,cy), 5, (255,0,0), thickness=2, lineType=8, shift=0)
p1=np.array([[x_v1*-scale*2, x_v1*scale*2],
         [y_v1*-scale*2, y_v1*scale*2]], int)
p2=np.array([[x_v2*-scale, x_v2*scale],
         [y_v2*-scale, y_v2*scale]], int)
print (p1)
cv2.line(black_img,(-346,200),(-200,346),(255,255,255),5)
cv2.imshow("black_img",black_img)
cv2.waitKey(0)
cv2.destroyAllWindows()