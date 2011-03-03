@app.route('/map')
def simple():
    bbox = mapnik.Envelope(
        mapnik.Coord(-20037508.34,
                     -20037508.34),
        mapnik.Coord(20037508.34,
                     20037508.34))
    return Response(
        render(map, bbox, 600, 600),
        content_type='image/png')
