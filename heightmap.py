from PIL import Image, ImageDraw
from colour import Color
import settings as s
import sys
import topng


def setpixel(x, y, value):
    img.putpixel((x, y), value)

def heightmap(hm, scale):
    SCALER = scale

    width, height = hm.size

    img = Image.new('I', (width // SCALER, height // SCALER), color='red')

    for y in range(0, height, SCALER):
        if y % (height // 100) == 0:
            print("hm", y / height * 100)
        for x in range(0, width // 2, SCALER):
            value = hm.getpixel((x, y))
            img.putpixel((x // SCALER * 2, y // SCALER), value)
            rightVal = hm.getpixel((x + width // 2, y))
            img.putpixel((x // SCALER * 2 + 1, y // SCALER), rightVal)

    return img

if __name__ == '__main__':
    directory = sys.argv[1]

    Image.MAX_IMAGE_PIXELS = 1061683200
    hm = Image.open("heightmap.tif")

    image = heightmap(hm, s.SCALE)
    image.save(directory + "/hm.tif")

    scaledpng = topng.to_png(image)
    scaledpng.save(directory + "/hm.png")
