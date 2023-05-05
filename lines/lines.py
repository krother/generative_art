
import numpy as np
from PIL import Image

def draw_line(a, xstart, ystart, xend, yend):
    assert xstart < xend
    x = np.arange(xstart, xend)
    slope = (yend - ystart) / (xend - xstart)
    y = ystart + ((x - xstart) * slope).round()
    y = y.astype(np.int32)
    a[y,x] = 255

a = np.zeros((400, 400), dtype=np.uint8)

for yend in range(0, 401, 50):
    draw_line(a, 50, 200, 350, yend)

im = Image.fromarray(a)
im.save('lines.png')
