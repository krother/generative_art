
import imageio
import numpy as np

a = imageio.imread("bbtor.jpg")

h, w = a.shape[0], a.shape[1]
Y, X = np.ogrid[0:h, 0:w]

mask = (X - w / 2) ** 2 + (Y - h / 2) ** 2 > w * h / 6

a[mask] = 0

imageio.imsave('mask.png', a)
