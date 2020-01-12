
# see video https://www.youtube.com/watch?time_continue=857&v=68ABAU_V8qI

import imageio
import numpy as np
from sklearn.mixture import GaussianMixture

a = imageio.imread("bbtor.jpg")[::8,::8]

y, x = np.mgrid[0:a.shape[0], 0:a.shape[1]]
#y, x = np.ogrid[0:a.shape[0], 0:a.shape[1]]

X = np.array([x.flatten(), y.flatten(), a[:,:,0].flatten(), a[:,:,1].flatten(), a[:,:,2].flatten()]).T
X.shape

m = GaussianMixture(n_components=40, covariance_type='full')
m.fit(X)
pred = m.sample(3000)[0]
blue = pred[pred[:,4]>100]
red = pred[pred[:,2]>100]
green = pred[pred[:,3]>100]
from matplotlib import pyplot as plt
plt.plot(blue[:,0], blue[:,1], 'b.')
plt.plot(green[:,0], green[:,1], 'g.')
plt.plot(red[:,0], red[:,1], 'r.')
plt.axis((0,240, 0, 160))
pred[pred > 255] = 255
pred[pred < 0] = 0

c = pred.reshape(a.shape).round().astype(np.uint8)
imageio.imsave('gaussian1.png', c)
