from PIL import Image, ImageDraw
from colour import Color
import settings as s
import sys
import colormap

import topng

HEIGHT = 29467
WIDTH = 128

img = Image.new('I', (WIDTH, HEIGHT), color=(-2147483648))


MAX = 1385517713
MIN = -563154762

stepsize = int((MAX - MIN) / HEIGHT)

print(stepsize)

map = []

for i in range(MIN, MAX - stepsize, stepsize):
    map.append(i)


line = 0
for value in map:
    print(line, value)

    for x in range(WIDTH):
        img.putpixel((x, line), value)

    line += 1

img.save("legend.tif")

image = colormap.colormap(img, s.gradient, s.smoothness)
image.save("colorlegend.png")
