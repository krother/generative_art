Meme Generator
==============

Let’s add some text to an image:

.. figure:: ../images/bridge_meme.png
   :alt: Bridge over Troubled Water

   Bridge over Troubled Water

NumPy cannot add text of its own. You need to use the ``Pillow`` library
instead:

.. literalinclude:: memegen.py

For the code to run, you need a **True-Type-Font (TTF)**. You can use
your own or `download arial.ttf <arial.ttf>`__.

To convert a Pillow Image to a Numpy array, use:

.. code:: python3

   a = np.array(im)

and back:

.. code:: python3
   
   im = Image.fromarray(a)

Challenge
---------

Add text to your own image to create a meme or inspirational image.
