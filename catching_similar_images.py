import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('C:\\Users\\ASHUU\\Desktop\\p1.PNG',0)
img2 = cv2.imread("C:\\Users\\ASHUU\\Desktop\\p2.PNG", 0)
cv2.imshow("image", img[0:600, 0:500])
cv2.imshow("image2", img2[0:600, 0:500])

image = img[0:337, 0:237]
image2 = img2[0:337, 0:237]
diff = image2-image
##result = not np.any(diff)
##
##if result is True:
##    print("the images are similar")
##else:
##    cv2.imshow("diff", diff)
##    print("the images are not similar")
