Puzzle
======

**The Numpy functions vstack and hstack concatenate arrays.**

|image0|

Assemble the complete picture from the images in :download:`pieces.zip`.

Here is the code that assembles two of the pieces:

.. literalinclude:: puzzle.py

Hints
-----

-  the functions ``np.vstack`` and ``np.hstack`` accept a list of NumPy
   arrays
-  one dimension of the arrays needs to be identical
-  use ``print(x.shape)`` a lot
-  the order in which you assemble matters

----

Challenge
---------

Create your own puzzle.
In :download:`make_pieces.py` you find code that was used to create pieces.


.. |image0| image:: ../images/puzzle_pieces.png

