import imageio
import numpy as np
from scipy import ndimage

b = imageio.imread("bbtor.jpg")[::2,::2]
b.shape
a = np.zeros((1200, 1200, 3), np.uint8)
s = b[200:440, 280:680]

a[200:440, 400:800] = s

r1 = ndimage.rotate(s, 120)
r2 = ndimage.rotate(s, 240)

x, y = 600, 440
a[y:y+r.shape[0], x-r.shape[1]:x] = r1
a[y:y+r.shape[0], x:x+r.shape[1]] = r2

c = a[::-2,::2]
a[240:840,300:900] |= c

imageio.imsave('caleidoscope.png', a)
