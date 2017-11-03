import cv2
import numpy as np
import imutils
import matplotlib.pyplot as plt

matrix_test = None
perimeters=[]
img=cv2.imread("Images/Circle.jpg",1)
img_height,img_width=img.shape[:2]
blur_img = cv2.bilateralFilter(img,1,75,75)
grey_img=cv2.cvtColor(blur_img,cv2.COLOR_BGR2GRAY)
_,thresh_img=cv2.threshold(grey_img,180,255,cv2.THRESH_BINARY)
black_image = np.zeros((img_height, img_width))

_,contours, hierarchy = cv2.findContours(thresh_img.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
contoursDraw=img.copy()
contoursDraw2=img.copy()


for i in contours:
	perimeter = cv2.arcLength(i,True)
	perimeters.append(perimeter)
	perimeters.sort()
	

cnt = contours[len(perimeters)-1]
M = cv2.moments(cnt)
print (M['m10'],M['m00'],M['m01'])
print(M)
cv2.drawContours(black_image,cnt,-1,(255,255,255), 1)


cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
center=np.array([cx,cy],float)
cv2.circle(contoursDraw2, (cx,cy), 5, (255,0,0), thickness=5, lineType=8, shift=0)
#print(center)

#Bounding Rectangle
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
cv2.drawContours(black_image,[box],0,(0,0,255),2)

y, x = np.nonzero(black_image)
x = x - np.mean(x)
y = y - np.mean(y)
coords = np.vstack([x, y])
cov = np.cov(coords)
evals, evecs = np.linalg.eig(cov)
sort_indices = np.argsort(evals)[::-1]
evec1, evec2 = evecs[:, sort_indices]
x_v1, y_v1 = evec1  # Eigenvector with largest eigenvalue
x_v2, y_v2 = evec2
scale = 200
plt.plot([x_v1*-scale*2, x_v1*scale*2],
         [y_v1*-scale*2, y_v1*scale*2], color='red')
plt.plot([x_v2*-scale, x_v2*scale],
         [y_v2*-scale, y_v2*scale], color='blue')
plt.plot(x, y, 'k.')
plt.axis('equal')
plt.gca().invert_yaxis()  # Match the image system with origin at top 
theta = np.tanh((x_v1)/(y_v1)) 
print (theta*57.295779513) 
rotation_mat = np.matrix([[np.cos(theta), -np.sin(theta)],
                      [np.sin(theta), np.cos(theta)]])
transformed_mat = rotation_mat * coords
# plot the transformed blob
x_transformed, y_transformed = transformed_mat.A
plt.plot(x_transformed, y_transformed, 'g.')																																							
plt.show()

p1=np.array([,])

for i in contours:
	#epsilon = 0.1*cv2.arcLength(i,True)
	#approx = cv2.approxPolyDP(i,epsilon,True)
	cv2.drawContours(contoursDraw,[i],-1,(0,255,0), 1)
	#getOrientation(contours[i], contoursDraw)


#cv2.imshow("img",img)
cv2.imshow("black_image",black_image)
cv2.imshow("thresh_img",thresh_img)
cv2.imshow("cDraw",contoursDraw)
cv2.imshow("contoursDraw2",contoursDraw2)
cv2.waitKey(0)
cv2.destroyAllWindows()