Infinite Blossom
================

|image0|

How does it work
----------------

The petals rotate around the center while getting closer.
Therefore, they are represented by **polar coordinates**: an angle and a distance.
The polar coordinates make the updating of petal positions very easy.
Of course, some trigonometric functions need to be applied to convert polar coordinates to cartesian (x/y) coordinates.

The animation happens on a canvas that is a lot bigger than the actual image.
This is because new petals appear regularly at the borders of the image, but that part is cropped off for better aesthetics.
The rest is optimizing the intervals in which the petals are places.

For drawing filled polygons I originally wanted to write a numpy function from scratch.
ChatGPT-3 told me there is a function `np.fill_poly()` and gave me a quite sophisticated code example.
It turned out it was hallucinating and no such function exists.
However, OpenCV has a fast enough function for drawing polygons.

Prerequisites
-------------

This script requires two libraries: **OpenCV** for displaying the live
animation and **imageio** for exporting animated GIFs.

::

   pip install opencv-python
   pip install imagio

The Script
----------

.. literalinclude:: blossom.py

.. |image0| image:: infinite_blossom.gif
