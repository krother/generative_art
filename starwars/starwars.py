"""

x0 = x - (xy) / (y-1)
y0 = -yc / (y-1)
"""
import numpy as np
import numpy as np
import cv2
import time
import imageio

YELLOW = (0, 255, 255)
WHITE = (255, 255, 255)

text = open('message.txt')

msg = np.zeros((3000, 1400, 3), np.uint8)
for y, line in enumerate(text):
    cv2.putText(msg, line.strip(), (50, y * 50 + 50), cv2.FONT_HERSHEY_TRIPLEX, fontScale=1.5, color=YELLOW, thickness=3)


indices = {}

# pre-calculate index arrays for each row
# to speed up display
c = 300
xx = np.arange(0, 1400)

for yy in range(1, 800):
    y = 1 - yy / 800
    y0 = int(-y * c / (y - 1))

    x = xx - 700
    x0 = (x - (x * y) / (y - 1)).astype(int)
    x0 += 600

    idx = np.where((x0 >= 0) * (x0 < 1400))
    src = x0[idx]
    dest = xx[idx]
    indices[yy] = (y0, src, dest)

ofs = 0
frames = []

background = np.zeros((800, 1400, 3), np.uint8)

while True:
    # display frames
    frame = background.copy()
    for yy in range(1, 800):
        y0, src, dest = indices[yy]
        if 0 <= y0 < 800:
            frame[yy][dest] = msg[-y0 + ofs][src]
    
    cv2.imshow('frame', frame)

    ofs += 1

    # shrink frame for using it on the web
    #rgb = cv2.cvtColor(frame[100:450:2, 200:-200:2], cv2.COLOR_BGR2RGB)
    #frames.append(rgb)

    key = chr(cv2.waitKey(1) & 0xFF)
    if key == 'q':
        break

    #time.sleep(0.03)

cv2.destroyAllWindows()

#imageio.mimsave('sand_animation.gif', frames[::2], fps=20)