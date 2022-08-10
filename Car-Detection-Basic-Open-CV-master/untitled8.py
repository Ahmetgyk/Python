import os
import re
import cv2 # opencv library
import numpy as np
from os.path import isfile, join
import matplotlib.pyplot as plt

imgs = []
rois = []

vidcap = cv2.VideoCapture('Pexels Videos 1572321.mp4')
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        imgs.append(image)
        rois.append(image[700: 2500,1500: 3000])
    return hasFrames

sec = 0
frameRate = 0.1
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)


for frame in [2, 3]:
    plt.imshow(cv2.cvtColor(imgs[frame], cv2.COLOR_BGR2RGB))
    plt.title("frame: "+str(frame))
    plt.show()

leng = len(rois) 
img1 = rois[1]
img2 = rois[2] 

for ls in range(leng - 1):
    grayA = cv2.cvtColor(rois[ls], cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(rois[ls + 1], cv2.COLOR_BGR2GRAY)
    diff_image = cv2.absdiff(grayB, grayA)
    ret, thresh = cv2.threshold(diff_image, 30, 255, cv2.THRESH_BINARY)
    kernel = np.ones((3,3),np.uint8)
    dilated = cv2.dilate(thresh,kernel,iterations = 1)

    plt.imshow(dilated)
    plt.show()

i = 458

blur = cv2.GaussianBlur(dilated,(5,5),0)
edges = cv2.Canny(blur,i, i*2)
result = img1.copy()
contours,hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(result, (x, y), (x+w, y+h), (255, 0, 0), 3)

cv2.imshow('output',result)
#cv2.imshow('input',dilated)
cv2.waitKey(0)
cv2.destroyAllWindows()