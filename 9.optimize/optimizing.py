# now lets optimize
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

# unpack left and right fit averages
def make_coordinates(image, line_parameters):
    slope, intercept = line_parameters
    # print(image.shape)
    y1 = image.shape[0]
    y2 = int(y1*(2/5))
    x1 = int((y1 - intercept) / slope)
    x2 = int((y2 - intercept) / slope)
    
    return(np.array([x1, y1, x2, y2]))
#
def average_slope_intercept(img, lines):
    left_fit = []
    right_fit = []
    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        parameters = np.polyfit((x1, x2), (y1, y2), 1)
        # print(parameters)
        slope = parameters[0]
        intercept = parameters[1]
        if slope < 0:
            left_fit.append((slope, intercept))
        else:
            right_fit.append((slope, intercept))
    # print(left_fit)
    # print(right_fit)
    left_fit_avg = np.average(left_fit, axis=0)
    right_fit_avg = np.average(right_fit, axis=0)
    # print(left_fit_avg)
    # print(right_fit_avg)
    left_line = make_coordinates(img, left_fit_avg)
    right_line = make_coordinates(img, right_fit_avg)
    return(np.array([left_line, right_line]))

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
canny_img = canny_method(lane_img)
cropped_img = region_of_interest(canny_img)
Lines = cv2.HoughLinesP(cropped_img, 2, np.pi/180, 100, np.array([]), 
                        minLineLength=40, maxLineGap=5)     

average_lines = average_slope_intercept(lane_img, Lines)  
line_img = display_lines(image,average_lines)

combo_img = cv2.addWeighted(lane_img, 0.8, line_img, 1, 1) 

cv2.imshow('result', combo_img)
cv2.waitKey(0)