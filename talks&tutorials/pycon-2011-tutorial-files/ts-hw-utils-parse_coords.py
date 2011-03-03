def parse_coords(tile_size, meta_size, zoom, x, y):
    """Transform tile offsets into queriable coordinates"""
    coords = [(x, y), (x + meta_size, y + meta_size)]
    coords = [[offset * float(tile_size) for offset in coord]
              for coord in coords]
    coords = [pixel2latlon(coord, zoom, tile_size) for coord in coords]
    coords = [mapnik.Coord(*coord) for coord in coords]
    coords = [projection.forward(coord) for coord in coords]
    return mapnik.Envelope(*coords)
