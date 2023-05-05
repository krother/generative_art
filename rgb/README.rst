Color
=====

With a three-dimensional array you get a RGB image.

|image0|

Here is the code that creates the image:

.. literalinclude:: rgb.py

.. note::

   -  the three dimensions are ``(y-size, x-size, colorchannel)``
   -  the third dimension has to have the size 3
   -  the three color channels are *red* ``[0]``, *green* ``[1]``, *blue*
      ``[2]``
   -  a 0 in a color channel means that color is inactive
   -  a 255 in a color channel means that the color is at maximum
      saturation

Using sliced assignments, you can modify each color channel separately.

----

Challenges:
-----------

-  create a pure green square
-  create a purple rectangle
-  create an orange rectangle
-  create a white image

|image1|

.. |image0| image:: ../images/pink.png
.. |image1| image:: ../images/rgb_challenge.png

