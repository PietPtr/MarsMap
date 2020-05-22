from PIL import Image, ImageDraw
from colour import Color

Image.MAX_IMAGE_PIXELS = 1061683200

hm = Image.open('hm.png')

SCALER = 1

width, height = hm.size

img = Image.new('RGBA', (width // SCALER, height // SCALER), color=(0, 0, 0, 0))

MAX = 1385517713
MIN = -513154762

SMOOTHNESS = 10

gradient = [
    (0, "#615c30"),
    (3, "#9d7c49"),
    (7, "#e4be6d"),
    (11, "#c85844"),
    (20, "#edc5b5")
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
    c = colors[colorIndex]
    color = ctot(c)
    img.putpixel((x, y), color)

for y in range(0, height, SCALER):
    for x in range(0, width // 2, SCALER):
        value = hm.getpixel((x, y))
        setpixel(x // SCALER * 2, y // SCALER, value)
        rightVal = hm.getpixel((x + width // 2, y))
        setpixel(x // SCALER * 2 + 1,y // SCALER, rightVal)
        # img.putpixel((x // SCALER * 2,y // SCALER), value)
        # img.putpixel((x // SCALER * 2 + 1,y // SCALER), hm.getpixel((x + width // 2, y)))


img.save("cm.png")
