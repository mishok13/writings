#!/usr/bin/env python


import mapnik
import sys

projections = {'mercator': ("+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 "
                            "+lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m "
                            "+nadgrids=@null +no_defs +over"),
               'mollweide': ("+proj=moll +x_0=0 +y_0=0 +a=6371000"
                             "+b=6371000 +units=m +no_defs")}

projection = mapnik.Projection(projections['mollweide'])


map = mapnik.Map(1200, 600)
mapnik.load_map(map, sys.argv[1])
image = mapnik.Image(1200, 600)
coords = mapnik.Coord(-179.999, -89.999), mapnik.Coord(179.999, 89.999)
bbox = mapnik.Envelope(projection.forward(coords[0]),
                       projection.forward(coords[1]))
print bbox
print mapnik.Envelope(mapnik.Coord(-175., -85.0), mapnik.Coord(175.0, 85.0)).forward(projection)
map.zoom_to_box(bbox)
mapnik.render(map, image)
with open(sys.argv[2], 'w') as f:
    f.write(image.tostring('png'))
