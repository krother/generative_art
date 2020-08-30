
from PIL import Image
import numpy as np

def circle(a, xcenter, ycenter, radius, color):
    Y, X = np.ogrid[0:400, 0:400]
    square_dist = (X - xcenter) ** 2 + (Y - ycenter) ** 2
    mask = square_dist < radius ** 2
    a[mask] = color

radius = 100
xcenter, ycenter = 200, 200
color = np.array([255, 128, 0], np.uint8)

a = np.zeros((400, 400, 3), np.uint8)
circle(a, xcenter, ycenter, radius, color)

im = Image.fromarray(a)
im.save('circle.png')
