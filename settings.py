import vectormath as vmath
import math
from PIL import Image, ImageDraw

Image.MAX_IMAGE_PIXELS = 1061683200

SCALE = 2

smoothness = 15
# gradient = [
#     (0, "#615b30"),
#     # (5, "#9f7d48"),
#     (12, "#ab8548"),
#     (17, "#dabe5a"),
#     (27, "#c87945"),
#     (50, "#d5c1ad")
# ]

gradient = [
    (0, "#260f00"),
    (5, "#502910"),
    (35, "#e3b88d"),
    (50, "#dfdad6")
]

sobelScale = -0.00000001

light = vmath.Vector3(1, 0.2, 0.8).normalize()

ambientPercentage = 0.12
