import sys, os
from pathlib import Path
from PIL import Image, ImageDraw
import vectormath as vmath

import heightmap
import projection
import colormap
import normalmap
import lightmap

import topng


directory = "output"
if len(sys.argv) > 1:
    directory = sys.argv[1]

Path("./" + directory).mkdir(parents=True, exist_ok=True)

Image.MAX_IMAGE_PIXELS = 1061683200
hm = Image.open('heightmap.tif')


SCALE = 60

scaled = heightmap.heightmap(hm, SCALE)
scaled.save(directory + "/hm.tif")

projected = projection.projectmap(scaled, SCALE)
projected.save(directory + "/pm.tif")

gradient = [
    (0, "#3b3d33"),
    (10, "#9d7c49"),
    (14, "#e4be6d"),
    (20, "#c85844"),
    (40, "#edc5b5")
]

colors = colormap.colormap(projected, gradient, 10)
colors.save(directory + "/cm.png")

scale = -0.00000001
normals = normalmap.normalmap(projected, scale)
normals.save(directory + "/nm.png")

light = vmath.Vector3(1, 0.2, 0.8).normalize()
shaded = lightmap.lightmap(normals, colors, light)
shaded.save(directory + "/map.png")



scaledpng = topng.to_png(scaled)
scaledpng.save(directory + "/hm.png")

projectedpng = topng.to_png(projected)
projectedpng.save(directory + "/pm.png")
