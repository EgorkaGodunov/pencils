import numpy as np
import cv2
import os

counter=0
for filename in os.listdir("images/"):
    if filename.endswith(('.jpg')):
        image = cv2.imread('images/'+filename)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        kernel = np.ones((6, 6), 'uint8')
        ret, thresh = cv2.threshold(gray,127,255,0)
        thresh = cv2.erode(thresh,kernel,iterations=14)
        contours, hierarchy  = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for i in contours:
            eps = 0.05 * cv2.arcLength(i,True)
            approx = cv2.approxPolyDP(i,eps,True)
            if len(approx)==2 and cv2.contourArea(i)>1000:
                counter+=1

print(f"penscils: {counter}")

