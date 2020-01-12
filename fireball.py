# http://www.partow.net/programming/bitmap/index.html#simpleexample09

from PIL import Image
import numpy as np
from math import pi, sin, cos
from random import randint

im = np.zeros((400, 400, 3), dtype=np.uint8)

fb_x = 200
fb_y = 200

colors = [
    np.array([255, 0, 0], np.float64),
    np.array([255, 128, 0], np.float64),
    np.array([255, 255, 0], np.float64),
    np.array([255, 255, 255], np.float64),
]

for i in range(4):
    # Draw circles with radii in the range [1,10]
    distortion = 0
    for ang in range(360):
        t = ang * pi / 180
        distortion += randint(0, 100) - 50
        for r in range(100 - i * 20):
            r += distortion / 50
            rx = int(r * sin(t) + fb_x)
            ry = int(r * cos(t) + fb_y)
            heat_distortion = 0#50.0 * cos(0.1 * i) + 50;

            val = colors[i] * 0.8 + heat_distortion + randint(1, 20)
            im[rx,ry] = val.astype(np.uint8)


Image.fromarray(im, 'RGB').save("fire.png")
