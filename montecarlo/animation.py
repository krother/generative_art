"""
creates an animated GIF from the MC-simulation
"""
import os
import imageio
from mosaic_generator import MosaicGenerator, TILE_SIZE, PATTERNS, COLORS

os.mkdir('frames')

patterns = get_patterns(size=TILE_SIZE, functions=PATTERNS, colors=COLORS)

    m = MosaicGenerator(INPUT_FILE, OUTPUT_SIZE, patterns)
    m.create_random_image()

# fit the model
for i in range(1, 100):
    m.optimize(i * 100)   # increasingly longer periods
    m.write_image(f'frames/{i}.png')

# create the GIF
images = []
for i in range(1, 100):
    filename = f'frames/{i}.png'
    images.append(imageio.imread(filename))

imageio.mimsave('output.gif', images, fps=20)
