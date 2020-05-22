from PIL import Image, ImageDraw
from colour import Color

Image.MAX_IMAGE_PIXELS = 1061683200

hm = Image.open('heightmap.tif')

SCALER = 30

width, height = hm.size

img = Image.new('I', (width // SCALER, height // SCALER), color='red')

MAX = 1385517713
MIN = -513154762

maxv = 0
minv = 0



def setpixel(x, y, value):
    # grey = int( ((value + (-MIN)) / (MAX + (-MIN))) * 255 )
    # color = (grey, grey, grey)
    img.putpixel((x, y), value)

for y in range(0, height, SCALER):
    progress = int((y / height) * 100)
    if (progress % 5 == 0):
        print(progress)
    for x in range(0, width // 2, SCALER):
        value = hm.getpixel((x, y))
        setpixel(x // SCALER * 2, y // SCALER, value)
        rightVal = hm.getpixel((x + width // 2, y))
        setpixel(x // SCALER * 2 + 1,y // SCALER, rightVal)
        # img.putpixel((x // SCALER * 2,y // SCALER), value)
        # img.putpixel((x // SCALER * 2 + 1,y // SCALER), hm.getpixel((x + width // 2, y)))


img.save("hm.tif")
