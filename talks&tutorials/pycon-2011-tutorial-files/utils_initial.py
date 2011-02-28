import mapnik

def project(coords, projection):
    """Reproject coords from WGS84 to given projection"""
    bbox = mapnik.Envelope(coords[0], coords[1])
    return bbox.forward(projection)

def render_map(map, bbox, width, height):
    """Render a map within a given bounding box and size"""
    map.resize(width, height)
    map.zoom_to_box(bbox)
    image = mapnik.Image(width, height)
    mapnik.render(map, image)
    return image.tostring('png')
