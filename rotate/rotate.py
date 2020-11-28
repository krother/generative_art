import imageio
import numpy as np
from scipy import ndimage

a = np.zeros((600, 600, 3), dtype=np.uint8)
rect = np.zeros((400, 400, 3), dtype=np.uint8)
blue = np.array([0, 127, 255])
rect[100:300,:] = blue // 9

for i in range(0, 180, 10):
    r = ndimage.rotate(rect, i)
    x = 300 - r.shape[1] // 2
    y = 300 - r.shape[0] // 2
    a[y:y+r.shape[0], x:x+r.shape[1]] += r

imageio.imsave('rotate.png', a)
