#!/usr/bin/env python


from flask import Flask, Response
import mapnik
import math
mapnik.register_plugins('/usr/lib/mapnik/input')


projection = mapnik.Projection("+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 "
                               "+lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m "
                               "+nadgrids=@null +no_defs +over")
map = mapnik.Map(0, 0)
mapnik.load_map(map, "map.xml")
app = Flask(__name__)


def render(map, bbox, width, height):
    map.resize(width, height)
    map.zoom_to_box(bbox)
    image = mapnik.Image(width, height)
    mapnik.render(map, image)
    return image.tostring('png')


def parse_coords(tile_size, meta_size, zoom, x, y):
    """Transform tile offsets into queriable coordinates"""
    coords = [(x, y), (x + meta_size, y + meta_size)]
    coords = [[offset * float(tile_size) for offset in coord]
              for coord in coords]
    coords = [pixel2latlon(coord, zoom, tile_size) for coord in coords]
    coords = [mapnik.Coord(*coord) for coord in coords]
    coords = [projection.forward(coord) for coord in coords]
    print coords
    return mapnik.Envelope(*coords)


def pixel2latlon(coord, zoom, tile_size=256):
    x, y = coord
    tile_size = float(tile_size)
    e = tile_size * 2**(zoom - 1)
    g = (e - y) * 2 * math.pi / (tile_size * 2**zoom)
    lat = (x - e) / ((tile_size * 2**zoom) / 360.0)
    lon = math.degrees((2 * math.atan(math.exp(g))) - (0.5 * math.pi))
    return lat, lon


@app.route('/')
def hello():
    return 'Hello world'


@app.route('/test')
def simple():
    bbox = mapnik.Envelope(mapnik.Coord(-20037508.34, -20037508.34),
                           mapnik.Coord(20037508.34, 20037508.34))
    try:
        return Response(render(map, bbox, 600, 600), content_type='image/png')
    except Exception, exc:
        print exc



@app.route('/<int:zoom>/<int:xtile>/<int:ytile>.<image_type>')
def tile(zoom, xtile, ytile, image_type):
    if image_type not in ('png', 'jpg'):
        raise
    metasize = 1 if zoom < 2 else 2
    bbox = parse_coords(256, metasize, zoom, xtile, ytile)
    try:
        return Response(render(map, bbox, 256, 256), content_type='image/png')
    except Exception, exc:
        print exc


@app.route('/<style_id>/<int:zoom>/<int:xtile>/<int:ytile>.<image_type>')
def styled_tile(style_id, zoom, xtile, ytile, image_type):
    pass



if __name__ == '__main__':
    app.run()
