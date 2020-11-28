
from PIL import Image
import numpy as np

a = np.array(Image.open("bbtor.jpg"))

mask = a[:,:,2] > 180

shadow = np.ones(a.shape, dtype=np.uint8) * 127
shadow[mask] = 255
shadow[20:, 20:] = shadow[:-20, :-20]

a[mask] = shadow[mask]
Image.fromarray(a, 'RGB').save("shadow.png")
