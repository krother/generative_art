"""
Runs a Monte Carlo Simulation to generate an image
close to a given target.
"""
import random
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt


# put your own image here
INPUT_FILE = "bbtor.jpg"
OUTPUT_FILE = "monte_carlo.png"
OUTPUT_SIZE = 960, 640

# play with these
ITERATIONS = 4000
MINW = 50
MAXW = 200


def load_target_image(fn, size):
    """returns the image as a NumPy array"""
    target = Image.open(fn)
    target = target.convert('RGB')
    print(f"read target image with size {target.size}")
    target = target.resize(size)
    return np.array(target, dtype=np.int16)

def get_random_rect(T):
    """Returns a random rectangle"""
    xcenter = random.randint(0, T.shape[1])
    ycenter = random.randint(0, T.shape[0])
    w = random.randint(MINW, MAXW)
    h = random.randint(MINW, MAXW)
    color = [random.randint(0, 255) for i in range(3)]
    x = max(0, xcenter - w // 2)
    y = max(0, ycenter - h // 2)
    return x, y, w, h, color

def get_distance(a, b):
    """the 'energy function' of the simulation"""
    return np.abs(a - b).sum()

def insert_rect_if_better(T, X, rect):
    """
    Core of the Monte Carlo procedure:
    Calculates the distance between the current and the target image
    for the given position.
    Then calculates the distance that the given pattern would result in.
    If the pattern lowers the distance, it is applied.
    """
    x, y, w, h, color = rect
    Xrect = X[y:y + h, x:x + h]
    Trect = T[y:y + h, x:x + h]

    patch = np.zeros(Xrect.shape)
    patch[:,:] = color

    old_dist = get_distance(Xrect, Trect)
    new_dist = get_distance(patch, Trect)
    if new_dist < old_dist:
        X[y:y + h, x:x + h] = patch


def optimize(T, X, iterations, history_interval=100):
    """
    Run a Monte Carlo optimization algorithm
    """
    assert X.shape == T.shape
    history = []
    for i in range(iterations):
        rect = get_random_rect(T)
        insert_rect_if_better(T, X, rect)
        if i % history_interval == 0:
            history.append(get_distance(X, T))
    return history


def write_image(X, out_fn):
    """Writes the output image to disk"""
    im = Image.fromarray(X.astype(np.uint8), 'RGB')
    im.save(out_fn)


if __name__ == '__main__':

    T = load_target_image(INPUT_FILE, OUTPUT_SIZE)
    X = np.zeros(T.shape, dtype=np.int16)

    history = optimize(T, X, ITERATIONS)
    write_image(X, OUTPUT_FILE)

    # plot the history of the loss function
    plt.plot(range(len(history)), history)
    plt.show()
