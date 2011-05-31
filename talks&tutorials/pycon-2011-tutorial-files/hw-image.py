map.zoom_to_box(layer.envelope())
image = Image(800, 400)
render(map, image)
with open('map.png', 'w') as image_file:
    image_file.write(image.tostring('png'))
