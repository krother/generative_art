from PIL import Image
import numpy as np

a = np.zeros((300, 500, 3), dtype=np.uint8)

a[100:200, 200:299, 0] = 255

im = Image.fromarray(a)
im.save('area.png')
