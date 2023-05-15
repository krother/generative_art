
import numpy as np
from PIL import Image
import math


def circle(a, xcenter, ycenter, radius, color):
    Y, X = np.ogrid[0:a.shape[0], 0:a.shape[1]]
    square_dist = (X - xcenter) ** 2 + (Y - ycenter) ** 2
    mask = square_dist < radius ** 2
    a[mask] = color


def spiral(    
        xcenter,
        ycenter,
        angle=0,
        radius=1,
        angle_step=10,
        radius_step=0.7
        ):
    """generates spiral coordinates"""
    while True:
        angle += angle_step
        radius += radius_step
        yield (
            round(math.cos(angle * math.pi / 180) * radius + xcenter),
            round(math.sin(angle * math.pi / 180) * radius + ycenter)
        )


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


a = np.zeros((800, 800, 3), dtype=np.uint8)
spiral_gen = spiral(
    xcenter=400,
    ycenter=400,
    angle=90,
    radius=1,
    angle_step=20,
    radius_step=6
)

for i in range(50):
    x, y = next(spiral_gen)
    radius = i // 2
    circle(a, x, y, radius, (0, abs(i*10 - 250), 0))
    circle(a, 800-x, 800-y, radius, (abs(i*10 - 250), 0, 0))


im = Image.fromarray(a)
im.save('spiral_challenge.png')
