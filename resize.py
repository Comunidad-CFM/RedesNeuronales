import PIL
from PIL import Image

basewidth = 333  # size
img = Image.open('./Imagenes/imagen.png')
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
img.save('imagen.jpg')
