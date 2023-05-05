
import time
import cv2
import numpy as np
import random

WHITE = 255, 255, 255
SIZE = 700


class BouncingBall:

    radius = 20
    color = WHITE

    def __init__(self):
        self.x = 100
        self.y = 100
        self.dx = 1
        self.dy = 1
    
    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x < 0:
            self.x = 0
            self.dx = random.randint(1, 3)
        if self.y < 0:
            self.y = 0
            self.dy = random.randint(1, 3)
        if self.x >= SIZE:
            self.dx = -random.randint(1, 3)
        if self.y >= SIZE:
            self.dy = -random.randint(1, 3)

    def draw(self, frame):
        Y, X = np.ogrid[0:SIZE, 0:SIZE]
        square_dist = (X - self.x) ** 2 + (Y - self.y) ** 2
        mask = square_dist < self.radius ** 2
        frame[mask] = self.color


bg = np.zeros((SIZE, SIZE, 3), dtype=np.uint8)
ball = BouncingBall()

while True:
    frame = bg.copy() // 2
    ball.move()
    ball.draw(frame)
    cv2.imshow('bouncing ball', frame)

    key = chr(cv2.waitKey(1) & 0xFF)
    if key == 'q':
        break

cv2.destroyAllWindows()
