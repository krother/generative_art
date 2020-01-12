
import imageio
import numpy as np

a = imageio.imread("bbtor.jpg")[::4,::4]
z = np.zeros((660, 980, 3), np.uint8)

z[:320, :480] = a[:,:,[2,0,1]]
z[:320, 500:] = a[:,:,[1,2,0]]
z[340:, :480] = a[:,:,[1,0,2]]
z[340:, 500:] = a[:,:,[2,1,0]]

imageio.imsave('colorchannels.png', z)
