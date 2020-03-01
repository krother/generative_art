
import imageio
import numpy as np

a = np.zeros((400, 400), dtype=np.uint8)
xcoord = np.random.randint(0, 399, size=(100))
ycoord = np.random.randint(0, 399, size=(100))

a[xcoord, ycoord] = 255

imageio.imsave('stars.png', a)
