def pixel2latlon(coord, zoom, tile_size=256):
    """Convert coordinate of pixel point to latitude, longitude"""
    x, y = coord
    tile_size = float(tile_size)
    e = tile_size * 2**(zoom - 1)
    g = ((e - y) * 2 * math.pi /
         (tile_size * 2**zoom))
    lat = ((x - e) /
           ((tile_size * 2**zoom) / 360.0))
    lon = math.degrees((2 * math.atan(math.exp(g)))
                       - (0.5 * math.pi))
    return lat, lon
