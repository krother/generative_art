
import numpy as np
import imageio

x = np.arange(200).reshape(200, 1)

a = x + x.T
a[a <= 200] = 1
a[a > 200] = 0
a *= 200

imageio.imsave('corner.png', a.astype(np.uint8))
