
from PIL import Image
import numpy as np

a = np.array(Image.open('a.png'))
b = np.array(Image.open('b.png'))
print(a.shape, b.shape)

im = np.vstack([a,b])  # vertical merge (correct)
print(im.shape)
Image.fromarray(im).save('vertical.png')

im = np.hstack([a,b])  # horizontal merge (WRONG)
print(im.shape)
Image.fromarray(im).save('horizontal.png')