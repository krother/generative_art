
import numpy as np
from PIL import Image

a = np.zeros((400, 400), dtype=np.uint8)
x = np.random.randint(0, 399, size=(100))
y = np.random.randint(0, 399, size=(100))

a[y, x] = 255

im = Image.fromarray(a)
im.save('stars.png')
