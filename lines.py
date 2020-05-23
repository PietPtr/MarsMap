from PIL import Image, ImageDraw
from colour import Color
import math
import settings as s
import sys
import topng
import projection
import drawSvg as draw

def lines(latstep, longstep, width, d, latorlong):

    if (latorlong is "long"):
        for long in range(-180, 181, longstep):
            points = []
            for lat in range(-90, 91, latstep):
                (x, y) = projection.robinson(lat, long, width / 6.1)
                points.append(x)
                points.append(y)
            d.append(draw.Lines(*points, close=False, fill='', stroke='black'))
    elif latorlong is "lat":
        for lat in range(-90, 91, latstep):
            points = []
            for long in range(-180, 181, longstep):
                (x, y) = projection.robinson(lat, long, width / 6.1)
                points.append(x)
                points.append(y)
            d.append(draw.Lines(*points, close=False, fill='', stroke='black'))



    return d


if __name__ == '__main__':
    directory = sys.argv[1]

    d = draw.Drawing(2000, 1000, origin='center', displayInline=False)

    fineness = 5

    lines(5, fineness, 1200, d, "long")
    lines(fineness, fineness, 1200, d, "lat")

    d.saveSvg(directory + "/lines.svg")

    # dots = lines(5, 30, 1200)
    # dots.save(directory + "/dots.png")

    # hm = Image.open(directory + "/hm.tif")
    #
    # image = lines(hm, 120)
    # projected = projection.projectmap(image, s.SCALE)
    # png = topng.to_png(projected)
    # png.save(directory + "/lines.png")
