
import imageio
import numpy as np

np.random.seed(42)
a = np.zeros((1680, 1680, 3), dtype=np.uint8)

for i in range(16):
    b = np.ones((400, 400, 3), dtype=np.uint8) * 255
    for j in range(20):
        r = np.random.randint(0, 400, size=7)
        x1, x2, y1, y2, c1, c2, c3 = tuple(r)
        x = min(x1,x2)
        y = min(y1,y2)
        w = abs(x2-x1)
        h = abs(y2-y1)
        b[y:y+h, x:x+w] = np.array([c1,c2,c3])
    ix = i % 4 * 420
    iy = i // 4 * 420
    a[iy:iy + 400, ix:ix + 400] = b

imageio.imsave('area.png', a)
