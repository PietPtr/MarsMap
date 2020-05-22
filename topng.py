from PIL import Image, ImageDraw
from colour import Color
import sys

Image.MAX_IMAGE_PIXELS = 1061683200

hm = Image.open(sys.argv[1])

SCALER = 1

width, height = hm.size

img = Image.new('RGBA', (width // SCALER, height // SCALER), color=(0, 0, 0, 0))

MAX = 1385517713
MIN = -513154762

maxv = 0
minv = 0



def setpixel(x, y, value):
    grey = int( ((value + (-MIN)) / (MAX + (-MIN))) * 255 )
    color = (grey, grey, grey)
    img.putpixel((x, y), color)

for y in range(0, height - SCALER, SCALER):
    progress = int((y / height) * 100)
    if (progress % 5 == 0):
        print(progress)
    for x in range(0, width - SCALER, SCALER):
        value = hm.getpixel((x, y))
        setpixel(x // SCALER, y // SCALER, value)

img.save(sys.argv[1].split('.')[0] + ".png")
