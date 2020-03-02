
import numpy as np
import imageio

a = np.zeros((300, 300, 3), dtype=np.uint8)

x = np.arange(200).reshape(200, 1)
y = x + x.T
y[y <= 200] = 1
y[y > 200] = 0

a[:200, :200, 0] = 200 * y
a[100:300, :200, 1] = 200 * y[::-1]
a[:200, 100:300, 2] = 200 * y[:,::-1]
a[100:300, 100:300, 0] = 200 * y[::-1,::-1]

imageio.imsave('triangles.png', a)
