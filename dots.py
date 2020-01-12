
import imageio
import numpy as np

a = np.zeros((400, 400), dtype=np.uint8)
xcoord = np.random.randint(0, 399, size=(10000))
ycoord = np.random.normal(200, 30, size=(10000)).astype(np.int32)

a[xcoord, ycoord] = 255

imageio.imsave('dots.png', a)
