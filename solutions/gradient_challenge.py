
from PIL import Image
import numpy as np

a = np.zeros((600, 600, 3), dtype=np.uint8)

full = np.zeros((200, 600), dtype=np.uint8)
full[:200, :] = np.linspace(0, 255, 600, dtype=np.uint8)

a[:200, :, 0] = full
a[400:, ::-1, 1] = full
a[400:, :, 2] = full

a[::-1, :200, 2] = full.T
a[:, 400:, 1] = full.T

im = Image.fromarray(a)
im.save('gradient_square.png')
