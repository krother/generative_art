
import pandas as pd
import pylab as plt
import numpy as np
from PIL import Image

GRIDSIZE = 30

panda = Image.open('panda.png')
panda = panda.convert('L')
panda = np.array(panda)

panda = 255 - panda # invert
df = pd.DataFrame(panda)

df = df.unstack()  # single column with x/y as index
df = df[df > 0]    # only non-white pixels

df = df.reset_index()
df.columns = ['x', 'y', 'col']  # for convenience
df['y'] *= -1  # otherwise matplotlib draws the panda upside-down

df = df.sample(df.shape[0] // 4)

df.plot.hexbin(x='x', y='y', gridsize=GRIDSIZE, cmap=plt.get_cmap('Greys'))
plt.savefig('hexpanda.png')
