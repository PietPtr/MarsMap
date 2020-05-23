import sys, os
from pathlib import Path
from PIL import Image, ImageDraw
import vectormath as vmath

import settings as s

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

hm = Image.open('heightmap.tif')


scaled = heightmap.heightmap(hm, s.SCALE)
scaled.save(directory + "/hm.tif")

projected = projection.projectmap(scaled, s.SCALE)
projected.save(directory + "/pm.tif")

colors = colormap.colormap(projected, s.gradient, s.smoothness)
colors.save(directory + "/cm.png")

normals = normalmap.normalmap(projected, s.sobelScale)
normals.save(directory + "/nm.png")

shaded = lightmap.lightmap(normals, colors, s.light, s.ambientPercentage)
shaded.save(directory + "/map.png")



scaledpng = topng.to_png(scaled)
scaledpng.save(directory + "/hm.png")

projectedpng = topng.to_png(projected)
projectedpng.save(directory + "/pm.png")
