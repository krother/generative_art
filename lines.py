
import numpy as np
import imageio

OUTPUT_FILE = "lines.png"

def draw_line(a, xstart, ystart, xend, yend):
    x = np.arange(xstart, xend)
    slope = (yend-ystart) / (xend-xstart)
    y = ystart + ((x-xstart) * slope).round().astype(np.int32)
    a[y,x] = 255

a = np.zeros((400, 400), dtype=np.uint8)
draw_line(a, 50, 50, 350, 50)
draw_line(a, 50, 50, 350, 350)
draw_line(a, 50, 50, 200, 350)
draw_line(a, 50, 50, 350, 200)

imageio.imsave('lines.png', a)
