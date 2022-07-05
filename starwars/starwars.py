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

text = open('message.txt')

msg = np.zeros((3000, 1400, 3), np.uint8)
for y, line in enumerate(text):
    cv2.putText(msg, line.strip(), (50, y * 50 + 50), cv2.FONT_HERSHEY_TRIPLEX, fontScale=1.5, color=YELLOW, thickness=3)

ofs = 0

frames = []
while True:
    # display frames
    background = np.zeros((800, 1400, 3), np.uint8)
    c = 400
    src_indices = []
    dest_indices = []
    for xx in range(1400):
        x = xx - 700
        for yy in range(1, 800):
            y = 1 - yy / 800
            x0 = int(x - (x * y) / (y - 1))
            y0 = int(-y * c / (y - 1))

            x0 += 600
            if (
                0 <= x0 < 1400 and
                0 <= y0 < 800
            ):
                src_indices.append((-y0*1400+x0))
                dest_indices.append(yy*1400 + xx)
                background[yy, xx] = msg[-y0 + ofs, x0]
    
    #src_indices = np.array(src_indices)
    #print(len(dest_indices))
    #background[tuple(dest_indices)] = 255#msg[tuple(src_indices + ofs*1400)]

    frame = background.copy()
    cv2.imshow('frame', frame)

    ofs += 10

    # shrink frame for using it on the web
    #rgb = cv2.cvtColor(frame[100:450:2, 200:-200:2], cv2.COLOR_BGR2RGB)
    #frames.append(rgb)

    key = chr(cv2.waitKey(1) & 0xFF)
    if key == 'q':
        break

    #time.sleep(0.03)

cv2.destroyAllWindows()

#imageio.mimsave('sand_animation.gif', frames[::2], fps=20)