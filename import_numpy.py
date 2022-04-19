# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 04:11:20 2022

@author: Asad"""


import numpy as np
import imageio
import cv2
from cv2 import imwrite
img = imageio.imread('C:/Users/Asad/.spyder-py3/images.jpg')
print(img)
print(img.dtype, img.shape)
img_tinted0 = img*[0., 255., 0.]
print(img_tinted0)
print(img_tinted0.dtype, img_tinted0.shape)

status = cv2.imwrite('C:/Users/Asad/.spyder-py3/images.jpg/img_tinted0.png',img_tinted0)
print("Image written to file-system : ",status)


#print(x, T)