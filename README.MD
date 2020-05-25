# Mars Relief Map Generator

Download the Digital Elevation Model made by the measurements of the Mars Global Surveyor [here](https://astrogeology.usgs.gov/search/details/Mars/GlobalSurveyor/MOLA/Mars_MGS_MOLA_DEM_mosaic_global_463m/cub), and save it as `heightmap.tif`.

In `settings.py` you can adjust scale, color gradient, and lighting settings.

Running `python map.py $directory` will then start generating the map. Rendering consists of a five step process. First the original heightmap is downscaled, since usually we don't need such a high resolution. Then the map is reprojected to the [Robinson projection](https://xkcd.com/977/). The third step is the generation of a color map. Based on the height data a color is picked from the gradient defined in the settings. After this a normal map is generated from the reprojected heightmap. Combining the normal map and the color map, lightmap will provide shading to generate the final product.

In the specified `$directory` the following files are generated:

* `hm.tif` and `hm.png`, the heightmap, both in TIF to preserve information for the next step and as a PNG to allow easy viewing.
* `pm.tif` and `pm.png`, the reprojected heightmap.
* `cm.png`, the color map.
* `nm.png`, the normalmap.
* `map.png`, the final shaded map.

To combine everything in a nice map, `annotations.svg` has the names of many different features and an overlay with lines showing latitudes and longitudes.

# License

All graphics files in this project are licensed under the CC-BY-SA 3.0.
All code in this project is licensed under the GPL version 3 or (at your option) any later version.
