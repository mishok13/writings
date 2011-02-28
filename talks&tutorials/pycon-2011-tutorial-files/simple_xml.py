from mapnik import render, Image, Map, load_map

map = Map(600, 600)
load_map(map, "simple-rendering-with-xml.xml")
map.zoom_to_box(map.layers[0].envelope())
image = Image(600, 600)
render(map, image)
with open('test.png', 'w') as f:
    f.write(image.tostring('png'))
