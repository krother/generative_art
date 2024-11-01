import numpy as np
import cv2
import math
import imageio
import time

BLACK = (0, 0, 0)

FRAME1 = 100
FRAME2 = 20
FRAME3 = 10

MAXX = 1800
MAXY = 800


def sine_move(start, end, frames, wait_frames=0):
    """
    smooth movement from a to b using a sine function.
    remain in end position forever
    """
    for _ in range(wait_frames):
        yield start
    for i in range(frames):
        angle_rad = i / frames * math.pi / 2
        if end > start:
            value = int(math.sin(angle_rad) * (end - start) + start)
        else:
            value = start - int(math.sin(angle_rad) * (start - end))
        yield value
    while True:
        yield value


def create_text():
    text = np.zeros((100, 300, 3), np.uint8) + 255
    return cv2.putText(
        text,
        "Python",
        (10, 50),
        cv2.FONT_HERSHEY_TRIPLEX,
        fontScale=1.5,
        color=BLACK,
        thickness=3,
    )


background = np.zeros((MAXY, MAXX, 3), np.uint8) + 255
blue = cv2.imread("blue.png")
yellow = cv2.imread("yellow.png")
ysize, xsize, _ = blue.shape
text = create_text()

frames = []
xgen = sine_move(0, 800, FRAME1)
ygen = sine_move(700, 420, FRAME2, wait_frames=FRAME1)
barcol = sine_move(start=255, end=150, frames=50, wait_frames=FRAME1 + FRAME2 + 5)
y = 200
while True:
    # display frames
    frame = background.copy()
    xblue = next(xgen)
    xyellow = 1600 - xblue
    frame[y : y + ysize, xblue : xblue + xsize] = blue
    frame[y : y + ysize, xyellow : xyellow + xsize] = (
        frame[y : y + ysize, xyellow : xyellow + xsize] & yellow
    )
    frame[y + ysize + 10 : y + ysize + 15, :] = next(barcol)
    ytext = next(ygen)
    frame[ytext : ytext + 100, 800:1100] = text
    frame = frame[:600, 400:-400]  # crop
    cv2.imshow("frame", frame)

    key = chr(cv2.waitKey(1) & 0xFF)
    if key == "q":
        break

    time.sleep(0.03)

    # shrink frame for using it on the web
    # rgb = cv2.cvtColor(frame[::2, ::2], cv2.COLOR_BGR2RGB)
    # frames.append(rgb)

cv2.destroyAllWindows()
# imageio.mimsave('logo_animation.gif', frames, fps=25)
