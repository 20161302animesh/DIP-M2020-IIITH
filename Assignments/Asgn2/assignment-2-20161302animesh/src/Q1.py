import cv2
import numpy as np
import os
import matplotlib
from matplotlib import pyplot as plt
os.chdir("../images/")

def filter_avg(im,k):
    n = k*k
    f = (np.ones([k,k]))/n
    img = np.array(im)
    h,w = img.shape
    d = int(k-1)
    m = int(d/2)
    imn = np.zeros(h+d,w+d)
    imn[m:h+m,m:w+m] = img[:,:]
    img_new = np.zeros([h,w])
    for i in range(m:h+m):
        for j in range(m:w+m):
            img_new[i,j] = sum(imn[i-m:i+m+1,j-m:j+m+1] * f)
    return img_new[i,j]
