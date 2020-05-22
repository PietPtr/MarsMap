from PIL import Image, ImageDraw
from colour import Color
import math

Image.MAX_IMAGE_PIXELS = 1061683200

hm = Image.open('hm.png')

HM_SCALER = 10
SCALER = 1

width, height = hm.size

img = Image.new('RGBA', (width // SCALER, height // SCALER), color=(0, 0, 0, 0))

rwidth, rheight = img.size

MAX = 1385517713
MIN = -513154762

maxv = 0
minv = 0

MAGIC = 10

def cylToLatLon(x, y):
    long = x / (128 / HM_SCALER)
    lat = y / (128 / HM_SCALER) - 90

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
def robinson(lat, long):
    idx = int(abs(lat) // 5)
    (X1, Y1) = robinsonTable[idx]
    (X2, Y2) = robinsonTable[idx + 1]

    diff = (abs(lat) - idx * 5) / 5
    X = X1 * (1 - diff) + X2 * (diff)
    Y = Y1 * (1 - diff) + Y2 * (diff)
    # X = X1
    # Y = Y2

    R = rwidth / 6.1

    x = 0.8487 * R * X * (long * RADS)
    y = math.copysign(1.3523 * R * Y, lat)

    return (x, y)


if __name__ == '__main__':
    for y in range(0, height, SCALER):
        if y % (height // 100) == 0:
            print(y / height * 100)
        for x in range(0, width, SCALER):
            color = hm.getpixel((x, y))
            (lat, long) = cylToLatLon(x - width / 2, y)
            (mapx, mapy) = robinson(lat, long)

            try:
                img.putpixel((int(mapx + rwidth / 2), int(mapy + rheight / 2)), color)
            except IndexError:
                pass




    img.save("robinson.png")
