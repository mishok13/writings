#!/usr/bin/env python


from flask import Flask, Response, request
from utils import project, render_map, parse_coords, tiles_in_bbox
import mapnik

projection = mapnik.Projection("+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 "
                               "+lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m "
                               "+nadgrids=@null +no_defs +over")
map = mapnik.Map(0, 0)
mapnik.load_map(map, "final.xml")

app = Flask(__name__)


@app.route('/')
def simple():
    bbox = mapnik.Envelope(mapnik.Coord(-20037508.34, -20037508.34),
                           mapnik.Coord(20037508.34, 20037508.34))
    return Response(render_map(map, bbox, 600, 600), content_type='image/png')


@app.route('/map/')
def staticmap():
    width = int(request.args.get('width', 600))
    height = int(request.args.get('height', 600))
    bbox = [float(x) for x in request.args['bbox'].split(',')]
    bbox = mapnik.Coord(bbox[0], bbox[1]), mapnik.Coord(bbox[2], bbox[3])
    bbox = project(bbox, projection)
    return Response(render_map(map, bbox, 600, 600), content_type='image/png')


@app.route('/<int:zoom>/<int:xtile>/<int:ytile>.<image_type>')
def tile(zoom, xtile, ytile, image_type):
    if image_type not in ('png', 'jpg'):
        raise
    metasize = 1 if zoom < 2 else 2
    bbox = parse_coords(256, metasize, zoom, xtile, ytile)
    return Response(render(map, bbox, 256, 256), content_type='image/png')


if __name__ == '__main__':
    app.run()
