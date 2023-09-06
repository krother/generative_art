
import math
import numpy as np
import cv2
import time
import imageio

MAXX, MAXY = 3000, 3000
SIZE = 5


class Petal:
    """
    Position of a petal in polar coordinates
    """
    def __init__(self, angle, dist):
        self.angle = angle
        self.dist = dist

    @property
    def moving(self):
        return self.dist > 0

    def update(self):
        self.angle += 1
        self.dist -= 1
    
    def polar_to_cartesian(self, angle, dist):
        rad = math.pi * angle / 180
        x = math.cos(rad) * dist
        y = math.sin(rad) * dist
        return int(y), int(x)

    def draw(self, frame):
        multiplier = 1.2 + self.dist / 200
        y1, x1 = self.polar_to_cartesian(self.angle, self.dist)
        y2, x2 = self.polar_to_cartesian(self.angle - 30, self.dist * multiplier)
        y3, x3 = self.polar_to_cartesian(self.angle + 30, self.dist * multiplier)

        col = (0, 64 - (64 * self.dist) // 360, 255 - (255 * self.dist)//360)

        offset = np.array([MAXY // 2, MAXX // 2])
        vertices = np.array([[y1, x1], [y2, x2], [y3, x3]]) + offset
        cv2.fillPoly(frame, [vertices], col)
        

def create_petals(dist, angle_offset=0):
    return [
        Petal(angle_offset + 0, dist),
        Petal(angle_offset + 120, dist),
        Petal(angle_offset + 240, dist),
    ]


background = np.zeros((MAXY, MAXX, 3), np.uint8)
petals = []
angle = 60
for dist in range(40, 400, 40):
    petals += create_petals(dist, angle)
    angle = 60 - angle


frames = []
angle_ofs = 0

for i in range(240):
    frame = background.copy()
    # more all petals
    for p in petals:
        p.update()
        p.draw(frame)
    petals = [p for p in petals if p.moving]  # remove finished petals

    cropped = frame[1200:-1200,1200:-1200]  # cut off border where new petals appear
    cv2.imshow('frame', cropped)
    rgb = cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB)
    frames.append(rgb)

    if i % 40 == 0:
        petals += create_petals(400, angle_ofs + i)
        angle_ofs = 60 - angle_ofs

    key = chr(cv2.waitKey(1) & 0xFF)
    if key == 'q':
        break

    time.sleep(0.03)

cv2.destroyAllWindows()

imageio.mimsave('infinite_blossom.gif', frames[::2], fps=20)