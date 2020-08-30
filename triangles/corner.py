
import numpy as np
from PIL import Image

x = np.arange(200).reshape(200, 1)

a = x + x.T
a[a <= 200] = 1
a[a > 200] = 0
a *= 200

im = Image.fromarray(a.astype(np.uint8))
im.save('corner.png')
