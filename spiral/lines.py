
import numpy as np
from PIL import Image


def draw_line(a, xstart, ystart, xend, yend):
    npoints = max(abs(xend - xstart) + 1, abs(yend - ystart) + 1)
    x = np.linspace(xstart, xend, npoints).round().astype(int)
    y = np.linspace(ystart, yend, npoints).round().astype(int)
    a[y, x] = 255
