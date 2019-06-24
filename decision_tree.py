"""
Example of using a Decision Tree
to remodel a photograph
"""
from sklearn.tree import DecisionTreeRegressor
from PIL import Image
import numpy as np
import pandas as pd

# Put your own file name here
INPUT_FILE = 'bbtor.jpg'
OUTPUT_FILE = 'output.png'

# Experiment with these parameters
SAMPLE_SIZE = 1000
DEPTH = 3

# read an input RGB image
im = Image.open(INPUT_FILE)
target = np.array(im)


# loop through color channels
result = target.copy()
for i in range(3):
    df = pd.DataFrame(target[:,:,i])
    df = df.stack().reset_index()
    df.columns = ['x', 'y', 'color']
    training = df.sample(SAMPLE_SIZE)

    # train a model that predicts the color from the coordinates
    X = training[['x','y']]
    m = DecisionTreeRegressor(max_depth=DEPTH)
    m.fit(X, training['color'])
    ypred = m.predict(df[['x', 'y']])  # predict on all data

    # merge the prediction into the result image
    result[:,:,i] = ypred.reshape((im.size[1], im.size[0]))

output = Image.fromarray(result)
output.save(OUTPUT_FILE)
