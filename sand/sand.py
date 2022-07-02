
import random
from traceback import format_exc
import numpy as np
import cv2
import time

BLACK = (0, 0, 0)
GRAY = (64, 64, 64)
WHITE = (255, 255, 255)
BEIGE = (128, 192, 255)

GRAIN_SIZE = 1

MAXX = 1200
MAXY = 550

class GrainOfSand:
    """
    generates sand coordinates
    """
    def __init__(self, x, y, xtarget):
        self._x = x
        self._y = y
        self.ymod = random.randint(-30, 30) / 10
        self.xtarget = xtarget
        self.speed = random.randint(-20, 20) / 10
        self.growth = 1.1
        self.delay = max(0, int(random.gauss(65, 20)))

    @property
    def x(self):
        return int(self._x)

    @property
    def y(self):
        return int(self._y)

    @property
    def finished(self):
        return self._x >= self.xtarget or self._y < 0 or self._y >= MAXY

    @property
    def moving(self):
        return self.delay == 0

    def update(self):
        if self.delay > 0:
            self.delay -= 1
        else:
            self._x += self.speed
            self._y += self.ymod
            if self.speed < 1.0:
                self.speed += 0.3
            else:
                self.speed *= self.growth


def draw_grain(frame, x, y, color):
    if x >= MAXX - 1: return
    frame[y:y+GRAIN_SIZE, x:x+GRAIN_SIZE] = color

def move_grains(frame, grains):
    for g in grains:
        g.update()

    # draw static grains
    for g in grains:
        if not g.moving:
            draw_grain(frame, g.x, g.y, BLACK)

    # draw moving grains
    for g in grains:
        if g.moving:
            draw_grain(frame, g.x, g.y, BEIGE)

    return [g for g in grains if not g.finished]


background = np.zeros((MAXY, MAXX, 3), np.uint8)
text = cv2.imread('desert_python.png')

# create grains
grains = []
for x in range(300, 900, GRAIN_SIZE):
    for y in range(200, 350, GRAIN_SIZE):
        grains.append(GrainOfSand(x, y, MAXX-2))

while True:
    frame = background.copy()
    frame[200:350, 300:853] = text
    grains = move_grains(frame, grains)

    cv2.imshow('frame', frame)

    key = chr(cv2.waitKey(1) & 0xFF)
    if key == 'q':
        break

    time.sleep(0.03)

cv2.destroyAllWindows()
