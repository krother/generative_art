
from PIL import Image
import numpy as np
from scipy.fftpack import fft, ifft

im = Image.open("bbtor.jpg").convert('L')
im = np.array(im).astype(np.float64)

a = fft(im, 1920, axis=1)

real = 255 * a.real/a.real.max()
imag = 255 * a.imag/a.imag.max()

ff = np.zeros((real.shape[0], real.shape[1], 3), dtype=np.uint8)
ff[:,:,0] = real.astype(np.uint8)
ff[:,:,1] = imag.astype(np.uint8)

Image.fromarray(ff, 'RGB').save("fft.png")
