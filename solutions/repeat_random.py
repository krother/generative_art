from PIL import Image
import random
import numpy as np

X_TILES = 32
Y_TILES = 12
TILE_WIDTH = 25
SPACING = 5
XSIZE = TILE_WIDTH * X_TILES + SPACING
YSIZE = TILE_WIDTH * Y_TILES + SPACING

a = np.zeros((YSIZE, XSIZE, 3), dtype=np.uint8)
a[:,:] = (128, 128, 128)

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

color_list = [random_color() for i in range(12)]
for x in range(X_TILES):
    for y in range(Y_TILES):
        random.shuffle(color_list)
        color = color_list[0]
        a[SPACING + y*TILE_WIDTH:(y+1)*TILE_WIDTH,
          SPACING + x*TILE_WIDTH:(x+1)*TILE_WIDTH] = color

im = Image.fromarray(a, 'RGB')
im.save("repeat.png")
im