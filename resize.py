import PIL
from PIL import Image

basewidth = 125  # size
img = Image.open('ironman.jpg')
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
img.save('ironmanOutPut.jpg')
