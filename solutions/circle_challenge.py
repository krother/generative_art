
import imageio
import numpy as np

def circle(a, xcenter, ycenter, radius, color):
    Y, X = np.ogrid[0:a.shape[0], 0:a.shape[1]]
    square_dist = (X - xcenter) ** 2 + (Y - ycenter) ** 2
    mask = square_dist < radius ** 2
    a[mask] = color

circles = [
    (250, np.array([127, 0, 0], np.uint8)),
    (200, np.array([255, 0, 0], np.uint8)),
    (175, np.array([255, 64, 0], np.uint8)),
    (150, np.array([255, 128, 0], np.uint8)),
    (125, np.array([255, 192, 0], np.uint8)),
    (100, np.array([255, 255, 0], np.uint8)),
    (75, np.array([255, 255, 127], np.uint8)),
    (50, np.array([255, 255, 255], np.uint8)),
]

a = np.zeros((1200, 1200, 3), np.uint8)
b = np.zeros((600, 600, 3), np.uint8)
c = np.zeros((600, 600, 3), np.uint8)
for r, col in circles:
    circle(b, 300, 300, r, col)
    circle(c, 300, 550-r, r, col)
    circle(a, 600+r, 600, r, col)
    circle(a, 600-r, 600, r, col)
    circle(a, 600, 600+r, r, col)
    circle(a, 600, 600-r, r, col)

imageio.imsave('circle_challenge.png', a)
imageio.imsave('circle_challenge2.png', b)
imageio.imsave('circle_challenge3.png', c)
