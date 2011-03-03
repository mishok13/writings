@app.route('/<int:zoom>/<int:xtile>'
           '/<int:ytile>.png')
def tile(zoom, xtile, ytile, image_type):
    metasize = 1 if zoom < 2 else 2
    bbox = parse_coords(256, metasize,
                        zoom, xtile, ytile)
    return Response(
        render(map, bbox, 256, 256),
        content_type='image/png')
