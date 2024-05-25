# a technique to find straight lines this technique is "HOUGH TRANSFORM".
import cv2
import numpy as np
import matplotlib.pyplot as plt

def canny_method(image):
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur_img = cv2.GaussianBlur(gray_img, (5, 5),0)
    canny = cv2.Canny(blur_img, 50, 150)
    return canny
 
def display_lines(img, lines):
    line_img = np.zeros_like(img)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(line_img, (x1, y1), (x2, y2), (255, 0, 0), 10)
    return line_img

def region_of_interest(image):
    height = image.shape[0]
    polygons = np.array([
    [(200, height), (1100, height), (550,250)]
    ])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 200)
    masked_image = cv2.bitwise_and(image, mask) 
    return masked_image

image = cv2.imread('test_image.jpg')
lane_img = np.copy(image)
canny = canny_method(lane_img)
cropped_img = region_of_interest(canny)
Lines = cv2.HoughLinesP(cropped_img, 2, np.pi/180, 100, np.array([]), 
                        minLineLength=40, maxLineGap=5)     
line_img = display_lines(image,Lines)

combo_img = cv2.addWeighted(lane_img, 0.8, line_img, 1, 1) #combine two images

cv2.imshow('result', combo_img)
cv2.waitKey(0)