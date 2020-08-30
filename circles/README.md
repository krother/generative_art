
# Circles

**Circles are drawn by calculating a 2D array of Euclidean distances and clipping:**

![](../images/circle.png)

Here is the code that creates the circle:

:::include circle.py

### Hints

* the `np.ogrid` function creates two 2D-array of the X/Y coordinates
* the `square_dist` contains the squared distance to the center for each pixel
* for the mask, the rule of Pythagoras is applied to select points inside the circle

----

## Challenge:

Adopt the code to create patterns from circles, e.g.:

![](../images/circle_challenge2.png)

![](../images/circle_challenge3.png)

![](../images/circle_challenge.png)
