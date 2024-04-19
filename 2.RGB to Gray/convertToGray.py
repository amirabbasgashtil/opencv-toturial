import cv2
import numpy as np

image = cv2.imread('test_image.jpg')

lane_img = np.copy(image)

# convert RGB image to gray
gray_img = cv2.cvtColor(lane_img, cv2.COLOR_BGR2GRAY)


cv2.imshow('result',gray_img)
cv2.waitKey(0)