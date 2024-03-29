
import numpy as np
from PIL import Image
import math


def interpolate(astart, aend, bstart, bend):
    """
    Returns arrays of x/y positions given start/end
    coordinates of a longer and shorter side
    """
    a = np.arange(astart, aend)
    slope = (bend - bstart) / (aend - astart)
    b = bstart + ((a - astart) * slope).round()
    b = b.astype(np.int32)
    return a, b


def draw_line(a, xstart, ystart, xend, yend, color):
    if xstart == xend:
        # vertical line
        x = xstart
        y = np.arange(*sorted((ystart, yend)))
    elif ystart == yend:
        # horizontal line
        x = np.arange(*sorted((xstart, xend)))
        y = ystart
    elif abs(xend - xstart) > abs(yend - ystart):
        # x wider than y
        (xstart, ystart), (xend, yend) = sorted([(xstart, ystart), (xend, yend)])
        x, y = interpolate(xstart, xend, ystart, yend)
    else:
        # y wider than x or same
        (ystart, xstart), (yend, xend) = sorted([(ystart, xstart), (yend, xend)])
        y, x = interpolate(ystart, yend, xstart, xend)
    a[y, x, color] = 255


a = np.zeros((500, 1200, 3), dtype=np.uint8)

for i in range(1, 1201, 10):
    xstart = 0
    ystart = 250
    xend = i
    color = i % 3
    yend = int(250 + math.sin(math.pi*xend/180) * 190)
    draw_line(a, xstart, ystart, xend, yend, color)

im = Image.fromarray(a)
im.save('naumgabo.png')
