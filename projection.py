from PIL import Image, ImageDraw
from colour import Color
import math
import settings as s
import sys
import topng

def cylToLatLon(x, y, scale):
    long = x / (128 / scale)
    lat = y / (128 / scale) - 90

    return (lat, long)

robinsonTable = [
	(1.0000,0.0000),
	(0.9986,0.0620),
	(0.9954,0.1240),
	(0.9900,0.1860),
	(0.9822,0.2480),
	(0.9730,0.3100),
	(0.9600,0.3720),
	(0.9427,0.4340),
	(0.9216,0.4958),
	(0.8962,0.5571),
	(0.8679,0.6176),
	(0.8350,0.6769),
	(0.7986,0.7346),
	(0.7597,0.7903),
	(0.7186,0.8435),
	(0.6732,0.8936),
	(0.6213,0.9394),
    (0.5722,0.9761),
    (0.5322,1.0000),
    (0.5322,1.0000)

]

RADS = math.pi / 180

# lat and long in degrees
def robinson(lat, long, R):
    idx = int(abs(lat) // 5)
    (X1, Y1) = robinsonTable[idx]
    (X2, Y2) = robinsonTable[idx + 1]

    diff = (abs(lat) - idx * 5) / 5
    X = X1 * (1 - diff) + X2 * (diff)
    Y = Y1 * (1 - diff) + Y2 * (diff)


    x = 0.8487 * R * X * (long * RADS)
    y = math.copysign(1.3523 * R * Y, lat)

    return (x, y)


def projectmap(hm, scale):
    width, height = hm.size

    img = Image.new('I', (width, height), color=(-2147483648))

    rwidth, rheight = img.size
    R = rwidth / 6.1

    for y in range(0, height):
        if y % (height // 100) == 0:
            print("pm", y / height * 100)
        for x in range(0, width):
            value = hm.getpixel((x, y))
            (lat, long) = cylToLatLon(x - width / 2, y, scale)
            (mapx, mapy) = robinson(lat, long, R)

            img.putpixel((int(mapx + rwidth / 2), int(mapy + rheight / 2)), value)

    return img


if __name__ == '__main__':
    directory = sys.argv[1]

    hm = Image.open(directory + "/hm.tif")

    image = projectmap(hm, s.SCALE)
    image.save(directory + "/pm.tif")

    scaledpng = topng.to_png(image)
    scaledpng.save(directory + "/pm.png")
