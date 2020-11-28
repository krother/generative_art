
from PIL import Image
import numpy as np

a = np.zeros((1025, 1025, 3), dtype=np.uint8)

for x in range(4):
    for y in range(4):
        color = (50 * y + 50, 50 * x + 50, 0)
        a[25 + y*250:(y+1)*250, 25 + x*250:(x+1)*250] = color

im = Image.fromarray(a, 'RGB')
im.save("color.png")
