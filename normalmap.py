from PIL import Image, ImageDraw
from colour import Color
import vectormath as vmath

def sobel(x, y, hm, sobelscale):
    s = []
    for ny in range(1, -2, -1):
        for nx in range(-1, 2):
            value = hm.getpixel((x + nx, y + ny))
            s.append(value)
            # if value != -2147483648:
            # else:
                # samples.append(hm.getpixel)

    normal = vmath.Vector3(0, 0, 0)
    scale = sobelscale
    normal.x = scale * -(s[2]-s[0]+2*(s[5]-s[3])+s[8]-s[6]);
    normal.y = scale * -(s[6]-s[0]+2*(s[7]-s[1])+s[8]-s[2]);
    normal.z = 1
    normal.normalize()

    normal.x = normal.x * 0.5 + 0.5
    normal.y = normal.y * 0.5 + 0.5
    normal.z = normal.z + 0.5

    return normal

def normalmap(hm, sobelscale):
    width, height = hm.size

    nm = Image.new('RGBA', (width, height), color=(0, 0, 0, 0))

    for y in range(0, height):
        if y % (height // 100) == 0:
            print("nm", y / height * 100)
        for x in range(0, width):
            value = hm.getpixel((x, y))
            if value != -2147483648:
                normal = sobel(x, y, hm, sobelscale)
                color = (\
                    int(normal.x * 255),
                    int(normal.y * 255),
                    int(normal.z * 255), 255)
                nm.putpixel((x, y), color)

    return nm
