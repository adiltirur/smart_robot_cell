import cv2
import numpy as np
import imutils

img=cv2.imread("Images/Square35.jpg",1)
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh_img=cv2.threshold(gray_img,220,255,cv2.THRESH_BINARY)
edged = cv2.Canny(thresh_img, 20, 100)
cnts = cv2.findContours(thresh_img.copy(), cv2.RETR_TREE,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[4]
print(cv2.__version__)
#print(cnts)
contourImage=img
contourImage=cv2.drawContours(contourImage,cnts,-1,255,3)
if len(cnts) > 0:
	# grab the largest contour, then draw a mask for the pill
	c = max(cnts, key=cv2.contourArea)
	mask = np.zeros(gray_img.shape, dtype="uint8")
	cv2.drawContours(mask, [c], -1, 255, -1)
 
	# compute its bounding box of pill, then extract the ROI,
	# and apply the mask
	(x, y, w, h) = cv2.boundingRect(c)
	imageROI = img[y:y + h, x:x + w]
	maskROI = mask[y:y + h, x:x + w]
	imageROI = cv2.bitwise_and(imageROI, imageROI,
		mask=maskROI)

cv2.imshow("img",img)
cv2.imshow("edged",edged)
cv2.imshow("mask",mask)

cv2.waitKey(0)
cv2.destroyAllWindows()