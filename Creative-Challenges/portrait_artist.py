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
    t = turtle.Turtle()
    turtle.tracer(0, 0)
    t.speed("fastest")
    for i, coords in enumerate(coordinates):
        start_coor, end_coor = coords[0], coords[1]
        t.penup()
        t.goto(start_coor)
        t.pendown()
        t.goto(end_coor)
        if i % 100 == 0:
            turtle.update()
    

def dodge(front,back):
    result=front*255/(255-back) 
    result[result>255]=255
    result[back==255]=255
    return result.astype('uint8')

def image_to_array():
    img = "Creative-Challenges\dave.jpg"
    s = imageio.imread(img)
    g=grayscale(s)
    i = 255-g
    b = scipy.ndimage.filters.gaussian_filter(i,sigma=10)
    r = dodge(b, g)
    plt.imshow(r, cmap="gray")
    plt.show()
    r = np.array(dodge(b,g))
    return r

def array_to_lines():
    array = image_to_array()
    coors = []
    for i, r in enumerate(array):
        for j, c in enumerate(r):
            if c >= 200:
                coors.append(((j-1, i-1), (j+1, i+1)))

    return coors

if __name__ == "__main__":
    draw_lines(array_to_lines())
