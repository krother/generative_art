
import numpy as np
from PIL import Image


def draw_line(a, xstart, ystart, xend, yend):
    npoints = max(abs(xend - xstart) + 1, abs(yend - ystart) + 1)
    x = np.linspace(xstart, xend, npoints).round().astype(int)
    y = np.linspace(ystart, yend, npoints).round().astype(int)
    a[y, x] = 255


a = np.zeros((400, 400), dtype=np.uint8)

for yend in range(0, 400, 50):
    draw_line(a, 50, 200, 350, yend)

im = Image.fromarray(a)
im.save('lines.png')
