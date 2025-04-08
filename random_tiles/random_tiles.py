
import numpy as np
from PIL import Image

a = np.random.randint(0, 255, size=(10, 10, 3), dtype=np.uint8)
a = np.kron(a, np.ones((20, 20, 1), dtype=a.dtype))

im = Image.fromarray(a)
im.save('random_colors.png')
