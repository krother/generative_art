
import numpy as np
from PIL import Image

a = np.random.randint(0, 255, size=(200, 200, 3), dtype=np.uint8)

im = Image.fromarray(a)
im.save('blur.png')
