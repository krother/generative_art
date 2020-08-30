
import numpy as np
from PIL import Image
import math

def draw_line(a, xstart, ystart, xend, yend, color):
    assert xstart < xend
    x = np.arange(xstart, xend)
    slope = (yend - ystart) / (xend - xstart)
    y = ystart + ((x - xstart) * slope).round().astype(np.int32)
    a[y, x, color] = 255

a = np.zeros((400, 1200, 3), dtype=np.uint8)

for i in range(1, 1201, 10):
    xstart = 0
    ystart = 200
    xend = i
    color = i % 3
    yend = int(ystart + math.sin(math.pi*xend/180) * 200)
    draw_line(a, xstart, ystart, xend, yend, color)

im = Image.fromarray(a)
im.save('naumgabo.png')
