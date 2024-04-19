# The goal is to identify the edges in our image
import cv2
import numpy as np

image = cv2.imread('test_image.jpg')
lane_img = np.copy(image)
gray_img = cv2.cvtColor(lane_img, cv2.COLOR_RGB2GRAY)
blur_img = cv2.GaussianBlur(gray_img, (5, 5),0)

# identifying the edges
canny = cv2.Canny(blur_img, 50, 150)

cv2.imshow('result',canny)
cv2.waitKey(0)