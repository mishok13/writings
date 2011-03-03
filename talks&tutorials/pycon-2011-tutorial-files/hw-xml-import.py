from mapnik import (Map, load_map,
                    Image, render)

map = Map(600, 600)
load_map(map, "simple.xml")
