from mapnik import render, Image, Map, load_map, Projection, Coord, Envelope


def project(coords, projection):
    """Reproject coords from WGS84 to given projection"""
    bbox = Envelope(coords[0], coords[1])
    return bbox.forward(projection)

def render_map(map, bbox, width, height):
    """Render a map within a given bounding box and size"""
    map.resize(width, height)
    map.zoom_to_box(bbox)
    image = Image(width, height)
    render(map, image)
    return image.tostring('png')

def load(file_path):
    """Load the Mapnik Map object using specified map file"""
    map = Map(0, 0)
    load_map(map, file_path)
    return map

def main():
    projection = Projection(
        "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 "
        "+lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m "
        "+nadgrids=@null +no_defs +over")
    coords = (Coord(-179.999999975, -85.0511287776),
              Coord(179.999999975, 85.0511287776))
    image = render_map(load("simple.xml"),
                       project(coords, projection), 600, 600)
    with open('test.png', 'w') as image_file:
        image_file.write(image)

if __name__ == '__main__':
    main()
