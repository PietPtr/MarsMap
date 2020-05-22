from PIL import Image, ImageDraw
from colour import Color
import vectormath as vmath


Image.MAX_IMAGE_PIXELS = 1061683200

nm = Image.open('nm.png')
cm = Image.open('cm.png')

width, height = nm.size
cwidth, cheight = cm.size

if cwidth != width or cheight != height:
    print("Resolutions do not match.")
    exit()

shaded = Image.new('RGBA', (width, height), color=(0, 0, 0, 0))


if __name__ == '__main__':
    for y in range(0, height):
        if y % (height // 100) == 0:
            print(y / height * 100)
        for x in range(0, width):
            (x, y, z, a) = nm.getpixel((x, y))
            print(a)
            if a is 255:
                color = cm.getpixel((x, y))

                print(x/255, y/255, z/255, color)

    nm.save("shaded.png")




print(sobel(293, 310))
