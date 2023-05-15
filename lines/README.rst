
.. _lines:

Lines
=====

Let’s draw lines:

|image0|

Here is the code that calculates lines between two points:

.. literalinclude:: lines.py


The algorithm calculates the number of points necessary to have at least one point on each x and y coordinate.
This is necessary because because it is unknown which of the dimensions is wider.

For calculating the coordinates, the function ``np.linspace`` does a great job at interpolating.
One tricky detail is that the numbers will be used for indexing the bigger array, so they have to be integers.
You need to remember rounding them before the conversion to int, otherwise you would see some strange artifacts.

.. note::
   
   The ``PIL.ImageDraw`` module contains a line drawing tool that
   allows you to draw thicker lines.   

----

Challenge
---------

Create line art (remotely inspired from the artist **Naum Gabo**)

|image1|

.. |image0| image:: lines.png
.. |image1| image:: ../images/naumgabo.png
