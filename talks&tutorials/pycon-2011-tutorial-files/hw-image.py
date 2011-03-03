m.zoom_to_box(layer.envelope())
image = Image(800, 400)
render(m, image)
with open('test.png', 'w') as image_file:
    image_file.write(image.tostring('png'))
