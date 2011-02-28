from flask import request
from utils import project

@app.route('/map/')
def staticmap():
    width = int(request.args.get('width', 600))
    height = int(request.args.get('height', 600))
    bbox = [float(x) for x in request.args['bbox'].split(',')]
    bbox = mapnik.Coord(bbox[0], bbox[1]), mapnik.Coord(bbox[2], bbox[3])
    bbox = project(bbox, projection)
    return Response(render_map(map, bbox, 600, 600), content_type='image/png')
