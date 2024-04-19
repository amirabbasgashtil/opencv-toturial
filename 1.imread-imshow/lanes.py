import cv2
# how to load an show images in opencv lib
image = cv2.imread('test_image.jpg')

cv2.imshow('result', image)
cv2.waitKey(0)