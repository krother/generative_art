Flags
=====

**Slicing NumPy arrays allows you to edit rectangular blocks of data.**

|image0|

Here is the code that carves out a red square from the image:

.. literalinclude:: flags.py

Hints
-----

   -  the slicing contains an interval ``from:to`` for each dimension
   -  the smallest ``from`` value is zero
   -  the highest ``to`` value is the size of that dimension plus one
   -  negative numbers count from the back
   -  both ``from`` and ``to`` can be omitted

----

Challenge
---------

Draw the flag of a country of your choice, e.g.:

|image1|

.. |image0| image:: ../images/slice.png
.. |image1| image:: ../images/finland.png
