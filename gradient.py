
import imageio
import numpy as np

a = np.zeros((600, 1200, 3), dtype=np.uint8)

full = np.linspace(0, 255, 1200, dtype=np.uint8)
half = np.linspace(0, 127, 1200, dtype=np.uint8)

a[:200, :, 0] = full
a[200:400, ::-1, 1] = full
a[400:, :, 1] = half
a[400:, :, 2] = full

imageio.imsave('gradient.png', a)
