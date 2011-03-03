"""Utilities used by imagery server"""


import mapnik
import math


def project(coords, projection):
    """Reproject coords from WGS84 to given projection"""
    bbox = mapnik.Envelope(coords[0], coords[1])
    return bbox.forward(projection)


def render(map, bbox, width, height):
    """Render a map within a given bounding box and size"""
    map.resize(width, height)
    map.zoom_to_box(bbox)
    image = mapnik.Image(width, height)
    mapnik.render(map, image)
    return image.tostring('png')


def parse_coords(tile_size, meta_size, zoom, x, y):
    """Transform tile offsets into queriable coordinates"""
    coords = [(x, y), (x + meta_size, y + meta_size)]
    coords = [[offset * float(tile_size) for offset in coord]
              for coord in coords]
    coords = [pixel2latlon(coord, zoom, tile_size) for coord in coords]
    coords = [mapnik.Coord(*coord) for coord in coords]
    coords = [projection.forward(coord) for coord in coords]
    return mapnik.Envelope(*coords)


def pixel2latlon(coord, zoom, tile_size=256):
    """Convert coordinate of pixel point to latitude, longitude"""
    x, y = coord
    tile_size = float(tile_size)
    e = tile_size * 2**(zoom - 1)
    g = (e - y) * 2 * math.pi / (tile_size * 2**zoom)
    lat = (x - e) / ((tile_size * 2**zoom) / 360.0)
    lon = math.degrees((2 * math.atan(math.exp(g))) - (0.5 * math.pi))
    return lat, lon
