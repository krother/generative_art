"""
source: https://stackoverflow.com/questions/37117878/generating-a-filled-polygon-inside-a-numpy-array
"""
import numpy as np
import imageio


def polygon(a, vertices):
    fill = np.ones(a.shape) * True
    idx = np.indices(a.shape)

    # loop over pairs of corner points
    for k in range(vertices.shape[0]):
        p1, p2 = vertices[k-1], vertices[k]
        dist = p2 - p1
        max_idx = (idx[0] - p1[0]) / dist[0] * dist[1] +  p1[1]
        sign = np.sign(dist[0])
        check = idx[1] * sign <= max_idx * sign
        fill = np.all([fill, check], axis=0)

    a[fill] = 127


# clockwise!
vertices = np.array([[50,120], [80,380], [230,240]])

a = np.zeros((400, 400), dtype=np.uint8)
polygon(a, vertices)

imageio.imsave('triangle.png', a)
