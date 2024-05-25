import cv2
import numpy as np
import matplotlib.pyplot as plt

def canny_method(image):
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur_img = cv2.GaussianBlur(gray_img, (5, 5),0)
    canny = cv2.Canny(blur_img, 50, 150)
    return canny

# creating the region of interest
def region_of_interest(image):
    height = image.shape[0]
    polygons = np.array([
    [(200, height), (1100, height), (550,250)]
    ])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 200)
    masked_image = cv2.bitwise_and(image, mask) # Bitwise_and operation
    return masked_image

image = cv2.imread('test_image.jpg')
lane_img = np.copy(image)
canny = canny_method(lane_img)
cropped_img = region_of_interest(canny)
#  regionOfInterest = region_of_interest(canny)
cv2.imshow('result',cropped_img)
cv2.waitKey(0)