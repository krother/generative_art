
from PIL import Image
from PIL import ImageDraw, ImageFont

im = Image.open('bridge.png')
draw = ImageDraw.Draw(im)
arial = ImageFont.truetype('arial.ttf', 30)

draw.text(
          (20, 390), 
          'All your dreams are on their way', 
          fill=('white'), 
          font=arial
          )
draw.text(
          (20, 430), 
          '(Simon & Garfunkel)', 
          fill=('white'),
          font=arial
          )

im.save('meme.png')

