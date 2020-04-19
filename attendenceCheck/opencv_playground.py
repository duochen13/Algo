import numpy as np 
import cv2

# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html#display-image

img = cv2.imread('test.png', 0)
cv2.imshow('window name', img)


