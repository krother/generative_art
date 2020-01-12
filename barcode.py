
import imageio
import numpy as np

a = np.ones((400, 400), dtype=np.uint8) * 255
xcoord = np.random.randint(0, 400, size=(100))

a[:, xcoord] = 0

imageio.imsave('barcode.png', a)
