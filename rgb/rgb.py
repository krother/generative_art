
import numpy as np
from PIL import Image

a = np.zeros((200, 200, 3), dtype=np.uint8)
a[:, :, 0] += 255
a[:, :, 2] += 128

im = Image.fromarray(a)
im.save('pink.png')
