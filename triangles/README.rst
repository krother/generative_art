Triangles
=========

Arithmetics on a vector with its own transpose results in a matrix.

Cropping selects a triangular section.

|image0|

.. literalinclude:: corner.py

Hints
-----

-  the code only works for triangles with two edges parallel to the axes
   of the coordinate system
-  the instruction ``a.T`` *transposes* the array
-  the conditional assignment allows you to set only a part of the
   values in an array

----

Challenge:
----------

Create multiple straight-edge triangles.

|image1|

.. |image0| image:: ../images/corner.png
.. |image1| image:: ../images/triangles.png

