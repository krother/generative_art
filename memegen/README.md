
# Meme Generator

Let's add some text to an image:

![Bridge over Troubled Water](../images/bridge_meme.png)

NumPy cannot add text of its own.
You need to use the `Pillow` library instead:

:::include memegen.py

For the code to run, you need a **True-Type-Font (TTF)**.
You can use your own or [download arial.ttf](arial.ttf).

To convert a Pillow Image to a Numpy array, use:

    :::python3
    a = np.array(im)

and back:

    :::python3
    im = Image.fromarray(a)


## Challenge

Add text to your own image to create a meme or inspirational image.
