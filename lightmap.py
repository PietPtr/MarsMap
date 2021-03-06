from PIL import Image, ImageDraw
from colour import Color
import vectormath as vmath
import settings as s
import sys

def lightmap(nm, cm, light, ambient):
    width, height = nm.size
    cwidth, cheight = cm.size

    if cwidth != width or cheight != height:
        print("Resolutions do not match.")
        exit()

    shaded = Image.new('RGBA', (width, height), color=(0, 0, 0, 0))

    for y in range(0, height):
        if y % (height // 100) == 0:
            print("lm", y / height * 100)
        for x in range(0, width):
            (cr, cg, cb, ca) = cm.getpixel((x, y))
            (r,g,b,a) = nm.getpixel((x, y))
            if a != 0:
                normal = vmath.Vector3(\
                    (r/255 - 0.5) * 2,
                    (g/255 - 0.5) * 2,
                    (b/255 - 0.5) * 2)
                angle = normal.angle(light, 'deg')
                illumination = 1 - (angle / 180)
                illumination = ambient + (1 - ambient) * illumination
                cr = int(illumination * cr)
                cg = int(illumination * cg)
                cb = int(illumination * cb)
                shaded.putpixel((x, y), (cr, cg, cb, ca))

    return shaded

if __name__ == '__main__':
    directory = sys.argv[1]
    nm = Image.open(directory + "/nm.png")
    cm = Image.open(directory + "/cm.png")

    image = lightmap(nm, cm, s.light, s.ambientPercentage)
    image.save(directory + "/map.png")
