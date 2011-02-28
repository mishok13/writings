#!/usr/bin/env python


from flask import Flask, Response
from utils import render_map
import mapnik

projection = mapnik.Projection("+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 "
                               "+lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m "
                               "+nadgrids=@null +no_defs +over")
map = mapnik.Map(0, 0)
mapnik.load_map(map, "map.xml")

app = Flask(__name__)


@app.route('/')
def simple():
    bbox = mapnik.Envelope(mapnik.Coord(-20037508.34, -20037508.34),
                           mapnik.Coord(20037508.34, 20037508.34))
    return Response(render_map(map, bbox, 600, 600), content_type='image/png')


if __name__ == '__main__':
    app.run()
