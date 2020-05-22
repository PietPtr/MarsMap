from PIL import Image, ImageDraw
from colour import Color
import vectormath as vmath


Image.MAX_IMAGE_PIXELS = 1061683200

hm = Image.open('robinson.tif')
cm = Image.open('cm.png')

width, height = hm.size
cwidth, cheight = cm.size

if cwidth != width or cheight != height:
    print("Resolutions do not match.")
    exit()

nm = Image.new('RGBA', (width, height), color=(0, 0, 0, 0))
shaded = Image.new('RGBA', (width, height), color=(0, 0, 0, 0))

def sobel(x, y):
    s = []
    for ny in range(1, -2, -1):
        for nx in range(-1, 2):
            value = hm.getpixel((x + nx, y + ny))
            s.append(value)
            # if value != -2147483648:
            # else:
                # samples.append(hm.getpixel)

    normal = vmath.Vector3(0, 0, 0)
    scale = 0.00000001
    normal.x = scale * -(s[2]-s[0]+2*(s[5]-s[3])+s[8]-s[6]);
    normal.y = scale * -(s[6]-s[0]+2*(s[7]-s[1])+s[8]-s[2]);
    normal.z = 1
    normal.normalize()

    normal.x = normal.x * 0.5 + 0.5
    normal.y = normal.y * 0.5 + 0.5
    normal.z = normal.z + 0.5

    return normal

if __name__ == '__main__':
    for y in range(0, height):
        if y % (height // 100) == 0:
            print(y / height * 100)
        for x in range(0, width):
            value = hm.getpixel((x, y))
            if value != -2147483648:
                normal = sobel(x, y)
                # print(normal)
                color = (\
                    int(normal.x * 255),
                    int(normal.y * 255),
                    int(normal.z * 255), 255)
                nm.putpixel((x, y), color)

    nm.save("nm.png")
