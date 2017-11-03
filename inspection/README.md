### Angle ###
Find angle of orientation of the image
Python 3.5.2
Opencv 3.2.0

Using the DXF(converted to JPEG) images of the parts or drawings generated from a CAD software.
Add a ROI for the better results.


Method 1(Using the contours detection on the image)
--Uses contour detection method and wraps the image to find the angle of the bounding box.
--Orientation is found for binary image.
--Change the 'threshVal' to change the value.

Method 2(Using PCA-Principal Component Analysis)
--