import vectormath as vmath

SCALE = 30

smoothness = 10
gradient = [
    (0, "#615b30"),
    # (5, "#9f7d48"),
    (12, "#ab8548"),
    (17, "#dabe5a"),
    (27, "#c87945"),
    (50, "#d5c1ad")
]

sobelScale = -0.000000015

light = vmath.Vector3(1, 0.2, 0.8).normalize()

ambientPercentage = 0.1
