from PIL import Image, ImageDraw
from colour import Color

Image.MAX_IMAGE_PIXELS = 1061683200

hm = Image.open('robinson.tif')

SCALER = 1

width, height = hm.size

img = Image.new('RGBA', (width // SCALER, height // SCALER), color=(0, 0, 0, 0))

MAX = 1385517713
MIN = -513154762

SMOOTHNESS = 10

gradient = [
    (0, "#615c30"),
    (4, "#9d7c49"),
    (11, "#e4be6d"),
    (20, "#c85844"),
    (40, "#edc5b5")
]

colors = []

for g in range(len(gradient) - 1):
    (start, color) = gradient[g]
    (nextStart, nextColor) = gradient[g+1]

    begin = start * SMOOTHNESS
    end = (nextStart - start) * SMOOTHNESS

    colorList = list(Color(color).range_to(Color(nextColor), end))
    colors += colorList


def ctot(c):
    return int(c.red * 255), int(c.green * 255), int(c.blue * 255)

def setpixel(x, y, value):
    colorIndex = int( ((value + (-MIN)) / (MAX + (-MIN))) * (len(colors) - 1) )
    try:
        c = colors[colorIndex]
    except IndexError:
        c = Color("#000000")

    color = ctot(c)
    img.putpixel((x, y), color)

for y in range(0, height, SCALER):
    if y % (height // 100) == 0:
        print(y / height * 100)
    for x in range(0, width, SCALER):
        value = hm.getpixel((x, y))
        if value != -2147483648:
            setpixel(x // SCALER, y // SCALER, value)


img.save("cm.png")
