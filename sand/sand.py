
import random
import numpy as np
import cv2
import time
import imageio

BLACK = (0, 0, 0)
BEIGE = (128, 192, 255)

GRAIN_SIZE = 3  # smaller looks better but also slower

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
        self.xspeed = random.randint(-20, 20) / 10
        self.xgrowth = 1.1  # multiplier for xspeed
        self.delay = max(0, int(random.gauss(65, 20)))

        # randomize color a little
        self.color = list(BEIGE)
        self.color[0] += random.randint(-50, 50)
        self.color[1] += random.randint(-50, 50)
        self.color[2] += random.randint(-50, 0)

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
            self.delay -= 1  # waiting time before grain starts to move
        else:
            self._x += self.xspeed
            self._y += self.ymod
            if self.xspeed < 1.0:  # redirect moves from left to right
                self.xspeed += 0.3
            else:
                self.xspeed *= self.xgrowth


def create_grains():
    grains = []
    for x in range(300, 900, GRAIN_SIZE):
        for y in range(200, 350, GRAIN_SIZE):
            grains.append(GrainOfSand(x, y, MAXX-2))
    return grains


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
            draw_grain(frame, g.x, g.y, g.color)

    return [g for g in grains if not g.finished]


background = np.zeros((MAXY, MAXX, 3), np.uint8)
text = cv2.imread('desert_python.png')
background[200:350, 300:853] = text
grains = create_grains()


frames = []
while True:
    # display frames
    frame = background.copy()
    grains = move_grains(frame, grains)
    cv2.imshow('frame', frame)

    # shrink frame for using it on the web
    rgb = cv2.cvtColor(frame[100:450:2, 200:-200:2], cv2.COLOR_BGR2RGB)
    frames.append(rgb)

    key = chr(cv2.waitKey(1) & 0xFF)
    if key == 'q':
        break

    #time.sleep(0.03)

cv2.destroyAllWindows()

    
imageio.mimsave('sand_animation.gif', frames[::2], fps=20)