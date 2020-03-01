"""
Cluster the colors of an image
"""
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

# put your own image here
INPUT_FILE = "bbtor.jpg"
OUTPUT_FILE = "output.png"
N_CLUSTERS = 6
N_SAMPLES = 100  # number of random pixels used for clustering


def cluster_transform(X):
    """cluster the colors of an image"""
    m = KMeans(N_CLUSTERS)
    indices = np.random.randint(0, X.shape[0]-1, size=N_SAMPLES)
    Xtrain = X[indices]
    m.fit(Xtrain)
    clusters = m.predict(X)
    c = [m.cluster_centers_[i] for i in clusters]
    return np.array(c)


if __name__ == '__main__':
    im = Image.open(INPUT_FILE)
    im = im.resize((im.size[0] // 2, im.size[1] // 2))

    a = np.array(im)
    a = a.reshape((a.shape[0] * a.shape[1], 3))
    c = cluster_transform(a)

    c = c.reshape(im.size[1], im.size[0], 3)
    im = Image.fromarray(c.astype(np.uint8), 'RGB')
    im.save(OUTPUT_FILE)
