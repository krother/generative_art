
from PIL import Image
import numpy as np

a = np.array(Image.open('../bbtor.jpg'))
a = a[::2, ::2]
print(a.shape)

left = a[:, :220]
right = a[:, 220:]

a = left[:-320]
b = left[-320:]

t2 = right[:500]
c = right[500:]

t3 = t2[:, :400]
d = t2[:, 400:]

e = t3[:200]
f = t3[200:]

Image.fromarray(a).save('a.png')
Image.fromarray(b).save('b.png')
Image.fromarray(c).save('c.png')
Image.fromarray(d).save('d.png')
Image.fromarray(e).save('e.png')
Image.fromarray(f).save('f.png')
