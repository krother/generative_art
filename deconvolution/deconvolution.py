
import numpy as np
from PIL import Image

KERNEL_Y, KERNEL_X = 9, 9
IMAGE_SIZE = 100, 100
FMAP_Y = IMAGE_SIZE[0] - KERNEL_Y + 1
FMAP_X = IMAGE_SIZE[1] - KERNEL_X + 1

FILTERS = 4

weights = np.random.random(size=(KERNEL_Y, KERNEL_X, FILTERS))
features = np.random.random(size=(FMAP_Y, FMAP_X, FILTERS))

line = np.zeros((KERNEL_Y, KERNEL_X))
line[:, 4] = 2.0

block = np.zeros((KERNEL_Y, KERNEL_X))
block[1:-1, 1:-1] = 1.0

weights[:,:,0] = line
weights[:,:,1] = line.T
weights[:,:,2] = block

a = np.zeros(IMAGE_SIZE)
for y in range(FMAP_Y):
    for x in range(FMAP_X):
        dec = features[y][x] * weights
        dec = dec.sum(axis=2)
        a[y:y+KERNEL_Y, x:x+KERNEL_X] += dec

# scale
a = a - a.min()
a = 255 * a / a.max()
a = a.astype(np.uint8)

im = Image.fromarray(a)
im.save('deconv.png')
