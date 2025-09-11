import numpy as np
from PIL import Image

a = np.zeros((800, 800, 3), dtype=np.uint8)


def square(a, xmin, xmax, ymin, ymax, n):
    b = xmin + (xmax - xmin) // 3
    c = xmin + (xmax - xmin) * 2 // 3
    d = ymin + (ymax - ymin) // 3
    e = ymin + (ymax - ymin) * 2 // 3
    a[d:e, b:c, 1] += 32
    if n > 0:
        # draw smaller squares recursively
        square(a, ..., ..., ..., ..., n - 1)
        ...

square(a, 0, 800, 0, 800, n=1)
im = Image.fromarray(a)
im.save("square.png")
