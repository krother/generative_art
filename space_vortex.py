
import imageio
import numpy as np
import cv2

class SpaceVortex:
    """
    Generates an animated vortex of random stars
    """
    def __init__(self, xsize, ysize, n_stars=100, speed=0.2):
        self.amp = np.random.randint(0, xsize//2 - 10, size=(n_stars)).astype(np.int32)
        self.phase = np.random.randint(0, 360, size=(n_stars)).astype(np.int32)

        self.ycoord = np.random.randint(0, ysize, size=(n_stars))
        self.angle = 0
        self.speed = speed
        self.xsize = xsize

    def step(self):
        """move the stars ahead"""
        self.angle += self.speed
        if self.angle >= 360:
            self.angle = 0

    def draw(self, frame):
        """draw stars into a np.array"""
        xx = self.xsize // 2 + np.round(np.cos(np.pi * (self.angle + self.phase) / 180) * self.amp).astype(np.int32)
        frame[self.ycoord, xx] = 255


stars = SpaceVortex(800, 600, n_stars=100, speed=0.1)

while True:
    frame = np.zeros((600, 800, 4), dtype=np.uint8)

    stars.step()
    stars.draw(frame)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()
