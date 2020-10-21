import turtle
import numpy as np
import imageio
import scipy.ndimage
import matplotlib.pyplot as plt
from PIL import Image

def grayscale(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

# Takes list of [((start_x, start_y), (end_x, end_y)), ((start_x, start_y), (end_x, end_y)), ((start_x, start_y), (end_x, end_y)) ...]
# and draws them onto canvas
def draw_lines(coordinates):
    pass

def dodge(front,back):
    result=front*255/(255-back) 
    result[result>255]=255
    result[back==255]=255
    return result.astype('uint8')

def image_to_array():
    img ="http://static.cricinfo.com/db/PICTURES/CMS/263600/263697.20.jpg"
    s = imageio.imread(img)
    g=grayscale(s)
    i = 255-g
    b = scipy.ndimage.filters.gaussian_filter(i,sigma=10)
    r = np.array(dodge(b,g))
    return r

def array_to_lines(array):
    coors = []
    for i, r in enumerate(array):
        for j, c in enumerate(r):
            if c >= 200:
                coors.append(((j-1, i-1), (j+1, i+1)))

    return coors

print(array_to_lines(image_to_array()))