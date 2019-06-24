
from itertools import combinations
from PIL import Image, ImageDraw

RAINBOW = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'white', 'black']
SPICED = ['#6e0096', '#aa0078', '#ff0000', '#ff6900', '#ffa028', '#ffffff']
GRAYSCALE = ['#000000', '#222222', '#444444', '#666666', '#888888', '#aaaaaa', '#cccccc', '#ffffff']

def full(im, d, col, size):
    return im

def horizontal(im, d, col, size):
    d.rectangle((0, 0, size, size//2), col)
    return im

def vertical(im, d, col, size):
    d.rectangle((0, 0, size//2, size), col)
    return im

def diagonal1(im, d, col, size):
    d.polygon((0, 0, size, 0, 0, size), col)
    return im

def diagonal2(im, d, col, size):
    d.polygon((0, 0, size, size, 0, size), col)
    return im

def diamond(im, d, col, size):
    d.polygon((0, size//2, size//2, 0, size, size//2, size//2, size), col)
    return im

def inset(im, d, col, size):
    d.rectangle((size//4, size//4, size-size//4, size-size//4), col)
    return im

def generate_patterns(colors, func, size):
    for col1, col2 in combinations(colors, 2):
        im = Image.new('RGB', (size, size), color=col1)
        d = ImageDraw.Draw(im)
        func(im, d, col2, size)
        yield im

FULL = [full]
MOSAIC = [full, horizontal, vertical, diagonal1, diagonal2, diamond, inset]



def get_patterns(size, functions=MOSAIC, colors=RAINBOW):
    """
    Returns a list of pattern tiles of the given sizes.

    size      : an integer
    functions : a list of functions
    colors    : a list of color strings or hex codes
    """
    patterns = []
    for f in functions:
        patterns += list(generate_patterns(colors, f, size))
    return patterns
