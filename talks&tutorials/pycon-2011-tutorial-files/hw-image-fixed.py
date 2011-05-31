map.zoom_to_box(bbox.forward(projection))
image = Image(600, 600)
render(map, image)
with open('test.png', 'w') as image_file:
    image_file.write(image.tostring('png'))
