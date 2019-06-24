"""
Creates mosaic images from an input image
and a set of tiles using a random sampling algorithm.
"""
import random
import numpy as np
from PIL import Image
from patterns import FULL, MOSAIC, RAINBOW, SPICED, GRAYSCALE, get_patterns
from matplotlib import pyplot as plt


# put your own image here
INPUT_FILE = "bbtor.jpg"
OUTPUT_FILE = "output.png"
OUTPUT_SIZE = 960, 640

# play with these
PATTERNS = MOSAIC   # also try FULL
COLORS = SPICED     # also try GRAYSCALE or RAINBOW (or your own list)
GRID = True
ITERATIONS = 20000
TILE_SIZE = 20


class MosaicGenerator:
    """
    generates mosaic images
    """
    def __init__(self, target_fn, size, patterns):
        self.size = size
        self.step = patterns[0].size[0]
        self.patterns = [np.array(p, dtype=np.int16) for p in patterns]
        self.history = []
        self.T = self.load_target_image(target_fn)
        self.X = None
        assert self.xsize % self.step == 0
        assert self.ysize % self.step == 0

    @property
    def xsize(self):
        return self.size[0]

    @property
    def ysize(self):
        return self.size[1]

    def load_target_image(self, fn):
        """returns the image as a NumPy array"""
        target = Image.open(fn)
        target = target.convert('RGB')
        print(f"read target image with size {target.size}")
        target = target.resize(self.size)
        return np.array(target, dtype=np.int16)

    def create_random_image(self):
        """Creates an image from random patterns"""
        self.X = np.zeros(self.T.shape, dtype=np.int16)
        for x in range(0, self.xsize, self.step):
            for y in range(0, self.ysize, self.step):
                pat = random.choice(self.patterns)
                self.X[y:y + self.step, x:x + self.step] = pat
        self.history = []

    def get_random_position(self):
        """Returns a random position on the grid"""
        x = random.randint(0, self.xsize - self.step)
        y = random.randint(0, self.ysize - self.step)
        return x, y

    def get_random_position_grid(self):
        """Returns a random position on the grid"""
        x = random.randint(0, self.xsize // self.step -1) * self.step
        y = random.randint(0, self.ysize // self.step -1) * self.step
        return x, y

    @staticmethod
    def get_dist(a, b):
        return np.abs(a - b).sum()

    def insert_pattern_if_better(self, pos, pattern):
        """
        Core of the Monte Carlo procedure:

        Calculates the distance between the current and the target image
        for the given position.
        Then calculates the distance that the given pattern would result in.

        If the pattern lowers the distance, it is applied.
        """
        x, y = pos
        current_tile = self.X[y:y + self.step, x:x + self.step]
        target_tile = self.T[y:y + self.step, x:x + self.step]
        old_dist = self.get_dist(current_tile, target_tile)
        new_dist = self.get_dist(pattern, target_tile)
        if new_dist < old_dist:
            self.X[y:y + self.step, x:x + self.step] = pattern


    def optimize(self, iterations, history_interval=100, grid=True):
        """
        Run a Monte Carlo optimization algorithm
        """
        assert self.X.shape == self.T.shape
        if grid:
            random_pos = self.get_random_position_grid
        else:
            random_pos = self.get_random_position

        for i in range(iterations):
            pos = random_pos()
            pat = random.choice(self.patterns)
            self.insert_pattern_if_better(pos, pat)
            if i % history_interval == 0:
                self.history.append(self.get_dist(self.X, self.T))

    def write_image(self, out_fn):
        """Writes the output image to disk"""
        im = Image.fromarray(self.X.astype(np.uint8), 'RGB')
        im.save(out_fn)



if __name__ == '__main__':
    patterns = get_patterns(size=TILE_SIZE, functions=PATTERNS, colors=COLORS)

    m = MosaicGenerator(INPUT_FILE, OUTPUT_SIZE, patterns)
    m.create_random_image()
    m.optimize(ITERATIONS)
    m.write_image(OUTPUT_FILE)

    # get the history of the loss function
    plt.plot(range(len(m.history)), m.history)
    plt.show()
