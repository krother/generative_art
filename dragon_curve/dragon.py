import numpy as np
from PIL import Image

LEFT, UP, RIGHT, DOWN = range(4)


def left(direction):
    """rotates the direction counter-clockwise"""
    return (direction + 3) % 4


def right(direction):
    """rotates the direction clockwise"""
    return (direction + 1) % 4


def forward(a, pos, dist, direction, color=0):
    """draws a line on the canvas"""
    x, y = pos
    if direction == RIGHT:
        a[y, x:x+dist] = color
        pos = x + dist, y
    elif direction == LEFT:
        a[y, x-dist:x] = color
        pos = x - dist, y
    elif direction == UP:
        a[y-dist:y, x] = color
        pos = x, y - dist
    elif direction == DOWN:
        a[y:y+dist, x] = color
        pos = x, y + dist
    return pos


def draw_sequence(a, sequence, pos, size, direction, color):
    """draws a sequence of L and R characters"""
    for char in sequence:
        pos = forward(a, pos, size, direction, color)
        if char == 'R':
            direction = right(direction)
        else:
            direction = left(direction)
    pos = forward(a, pos, size, direction, color)


def invert(seq):
    return ''.join(['L' if char == 'R' else 'R' for char in seq])


def dragon(fwd, depth):
    if depth == 0:
        return fwd
    else:
        bwd = invert(reversed(fwd))
        return dragon(fwd + 'R' + bwd, depth-1)


dragon('R', 4)

a = np.zeros((600, 850, 3), dtype=np.uint8)
lightblue = (0, 128, 255)

seq = dragon('R', 12)
draw_sequence(a, seq,
              pos=(500, 150),
              size=4,
              direction=UP,
              color=lightblue)

im = Image.fromarray(a)
im.save('dragon.png')
