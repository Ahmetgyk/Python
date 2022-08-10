import cv2
import numpy as np   

img = cv2.imread('IMG_E4619.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)

edges = cv2.Canny(blur,250, 500)
result = img.copy()
contours,hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(result, (x, y), (x+w, y+h), (255, 0, 0), 3) # draw rectangle in blue color)

cv2.imshow('output',result)
cv2.waitKey(0)
cv2.destroyAllWindows()