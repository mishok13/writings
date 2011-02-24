#!/usr/bin/env python


import mapnik


projection = mapnik.Projection("+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 "
                               "+lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m "
                               "+nadgrids=@null +no_defs +over")


map = mapnik.Map(600, 600)
mapnik.load_map(map, 'map.xml')
image = mapnik.Image(600, 600)
coords = mapnik.Coord(-179.9999, -85), mapnik.Coord(179.9999, 85)
bbox = mapnik.Envelope(projection.forward(coords[0]),
                       projection.forward(coords[1]))
print bbox
map.zoom_to_box(bbox)
mapnik.render(map, image)
with open('map.png', 'w') as f:
    f.write(image.tostring('png'))
