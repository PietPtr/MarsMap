import vectormath as vmath
import math
from PIL import Image, ImageDraw

Image.MAX_IMAGE_PIXELS = 1061683200

SCALE = 30

smoothness = 15

gradient = [
    (0, "#502910"),
    (35, "#e3b88d"),
    (50, "#dfdad6")
]

sobelScale = -0.000000034

light = vmath.Vector3(1, 0.2, 0.8).normalize()

ambientPercentage = 0.12
