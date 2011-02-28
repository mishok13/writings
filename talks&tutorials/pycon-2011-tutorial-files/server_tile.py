from utils import parse_coords

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
