from mapnik import render, Image, Map, load_map, Projection, Coord, Envelope

projection = Projection("+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 "
                        "+lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m "
                        "+nadgrids=@null +no_defs +over")


map = Map(600, 600)
load_map(map, "simple-rendering-with-xml.xml")
bbox = Envelope(Coord(-179.999999975, -85.0511287776),
                Coord(179.999999975, 85.0511287776))
map.zoom_to_box(bbox.forward(projection))
image = Image(600, 600)
render(map, image)
with open('test.png', 'w') as f:
    f.write(image.tostring('png'))