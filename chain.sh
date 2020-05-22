# Produces the following images:
# hm.tif - a TIF version of the heightmap (smaller than the 2GB original)
# robinson.tif - a robinson projected version of hm.tif
# cm.png - a colored version of robinson.tif
# nm.png - normal map

# hm.png - PNG version of the TIF
# robinson.png - PNG version of the TIF

# make sure to set the SCALER right in heightmap.py and projection.py
python heightmap.py
python projection.py
python colormap.py
python normalmap.py

python topng.py hm.tif
python topng.py robinson.tif
