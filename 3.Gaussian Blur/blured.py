# Goal is to reduce Noise of image

import cv2
import numpy as np

image = cv2.imread('test_image.jpg')

lane_img = np.copy(image)

# convert RGB image to gray
gray_img = cv2.cvtColor(lane_img, cv2.COLOR_RGB2GRAY)

# blur the image
blur_img = cv2.GaussianBlur(gray_img, (5, 5),0)

cv2.imshow('result',blur_img)
cv2.waitKey(0)