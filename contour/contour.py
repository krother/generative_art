
import numpy as np
from PIL import Image


# create a 400 x 400 grid
dim = np.linspace(-10, 10, 400)
x, y, _ = np.meshgrid(dim, dim, [1])  # the [1] adds an extra dimension

# positions and widths of the 'hills'
position_x = np.array([-3.0, 7.0, 9.0])     
position_y = np.array([0.0, 8.0, -9.0]) 
width_x = np.array([5.3, 8.3, 4.0]) 
width_y = np.array([6.3, 5.7, 4.0])

# calculate height as a combination of Gaussians
d = np.sqrt(((x - position_x) / width_x) ** 2 + ((y - position_y) / width_y) ** 2)
z = np.exp(-d ** 2)  # shape is (400, 400, 3) because we have 3 hills


z = z.sum(axis=2)   # add the hills to get a single landscape
znorm = (z - z.min()) / (z.max() - z.min()) # normalize to range (0.0 .. 1.0)

# contour lines
contour = (znorm * 8).astype(np.uint8) * 32
im = Image.fromarray(contour, mode='L')
im.save('contour_steps.png')

# isolines
isolines = ((znorm * 100).round() % 16) == 0
isolines = (isolines * 255).astype(np.uint8)
im = Image.fromarray(isolines, mode='L')
im.save('contour_isolines.png')
