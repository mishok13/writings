def render(map, bbox, width, height):
    """Render a map within a given bounding box and size"""
    map.resize(width, height)
    map.zoom_to_box(bbox)
    image = mapnik.Image(width, height)
    mapnik.render(map, image)
    return image.tostring('png')
