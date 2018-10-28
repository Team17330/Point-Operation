import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('pun.jpg',0)
cv2.imshow('Original',img)

ret, th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
plt.subplot(311),plt.imshow(th1,'gray'),plt.title("Threshold 127")

ret, th1 = cv2.threshold(img,200,255,cv2.THRESH_BINARY)
plt.subplot(312),plt.imshow(th1,'gray'),plt.title("Threshold 200")

ret, th1 = cv2.threshold(img,70,255,cv2.THRESH_BINARY)
plt.subplot(313),plt.imshow(th1,'gray'),plt.title("Threshold 70")

plt.show()

