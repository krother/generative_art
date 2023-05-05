Edge Detection
==============

|image0|

The **Sobel Operator** is a simple procedure for detecting edges in an
image. It uses two *convolutional kernels* (3x3 matrices) that are run
over the image. The result of the sobel operator is the Euclidean length
of the dot products from both kernels.

To my understanding, running the double for loop over the image is very
hard to avoid. But I am happy to get myself disproved.

.. literalinclude:: sobel.py

----

Challenges
----------

-  Try your own image
-  Use only one of the kernels, so that you detect horizontal *or*
   vertical lines
-  Apply the Sobel operator on one color channel at a time

.. |image0| image:: ../images/sobel.png

