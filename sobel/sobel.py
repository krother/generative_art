
from PIL import Image
import numpy as np

im = Image.open('../bbtor.jpg').convert('L')

a = np.array(im)[::2, ::2]

gx = np.array([[-1, 0, 1],
               [-2, 0, 2],
               [-1, 0, 1]])

gy = np.array([[-1, -2, -1],
               [ 0,  0,  0],
               [ 1,  2,  1]])

sobel = np.zeros(a.shape)

for y in range(a.shape[0]-2):
    for x in range(a.shape[1]-2):
        sx = np.sum(gx * a[y:y+3, x:x+3])
        sy = np.sum(gx * a[y:y+3, x:x+3])

        sobel[y, x] = np.sqrt(sx**2 + sy**2)

snorm = 255 * sobel / sobel.max()
	
b = snorm.astype(np.uint8)
im = Image.fromarray(b)
im.save('sobel.png')
