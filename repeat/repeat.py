from PIL import Image
import numpy as np

N_TILES = 4
TILE_WIDTH = 125
SPACING = 15
SIZE = TILE_WIDTH * N_TILES + SPACING

a = np.zeros((SIZE, SIZE, 3), dtype=np.uint8)

for x in range(N_TILES):
    for y in range(N_TILES):
        color = (50 * y + 50, 50 * x + 50, 0)
        a[
            SPACING + y * TILE_WIDTH : (y + 1) * TILE_WIDTH,
            SPACING + x * TILE_WIDTH : (x + 1) * TILE_WIDTH,
        ] = color

im = Image.fromarray(a, "RGB")
im.save("repeat.png")
