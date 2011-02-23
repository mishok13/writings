#!/usr/bin/env python


from flask import Flask
import mapnik


projection = mapnik.Projection("+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 "
                               "+lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m "
                               "+nadgrids=@null +no_defs +over")
map = mapnik.Map(0, 0)
mapnik.load_map(map, "map.xml")
app = Flask(__name__)


def render(map, bbox, width, height):
    map
    map.resize(width, height)
    image = mapnik.Image(width, height)
    mapnik.render(map, image)
    return image.tostring('png')


def parse_coords(tile_size, meta_size, zoom, x, y):
    """Transform tile offsets into queriable coordinates"""
    coords = [(x, y), (x + meta_size, y + meta_size)]
    coords = [[offset * float(tile_size) for offset in coord]
              for coord in coords]
    coords = [utils.pixel2latlon(coord, zoom, tile_size) for coord in coords]
    coords = [mapnik.Coord(*coord) for coord in coords]
    coords = [projection.forward(coord) for coord in coords]
    return coords



@app.route('/')
def main():
    return 'Hello world'


@app.route('/<int:zoom>/<int:xtile>/<int:ytile>.<image_type>')
def tile(zoom, xtile, ytile, image_type):
    if image_type not in ('png', 'jpg'):
        raise
    bbox =
    return render(map, 256, 256)

@app.route('/<style_id>/<int:zoom>/<int:xtile>/<int:ytile>.<image_type>')
def styled_tile(style_id, zoom, xtile, ytile, image_type):
    pass



if __name__ == '__main__':
    app.run()
