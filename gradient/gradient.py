
from PIL import Image
import numpy as np

a = np.zeros((300, 1200, 3), dtype=np.uint8)

full = np.zeros((100, 1200), dtype=np.uint8)
full[:100, :] = np.linspace(0, 255, 1200, dtype=np.uint8)

half = np.zeros((100, 1200), dtype=np.uint8)
half[:100, :] = np.linspace(0, 127, 1200, dtype=np.uint8)

a[:100, :, 0] = full
a[100:200, ::-1, 1] = full
a[200:, :, 1] = half
a[200:, :, 2] = full

im = Image.fromarray(a)
im.save('gradient.png')
