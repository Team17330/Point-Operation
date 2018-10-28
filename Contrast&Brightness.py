import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('pun.jpg')
cv2.imshow('Original',img)

a1 = 1.5 #increase contrast 50% (time 1.5)
b1 = 50 #increase brightness 10units (plus 50)
c1 = cv2.addWeighted(img, a1, np.zeros(img.shape, img.dtype), 0, b1)
cv2.imshow('Increase contrast 50% & Increase brightness 50unit',c1)

a2 = 0.5 #decrease contrast 50% (time 0.5)
b2 = 50 #increase brightness 10units (plus 50)
c2 = cv2.addWeighted(img, a2, np.zeros(img.shape, img.dtype), 0, b2)
cv2.imshow('Decrease contrast 50% & Increase brightness 50unit',c2)

a3 = 1.5 #increase contrast 50% (time 1.5)
b3 = -50 #decrease brightness 10units (minus 50)
c3 = cv2.addWeighted(img, a3, np.zeros(img.shape, img.dtype), 0, b3)
cv2.imshow('Increase contrast 50% & Decrease brightness 50unit',c3)

a4 = 0.5 #decrease contrast 50% (time 0.5)
b4 = -50 #decrease brightness 10units (minus 10)
c4 = cv2.addWeighted(img, a4, np.zeros(img.shape, img.dtype), 0, b4)
cv2.imshow('Decrease contrast 50% & Decrease brightness 50unit',c4)
