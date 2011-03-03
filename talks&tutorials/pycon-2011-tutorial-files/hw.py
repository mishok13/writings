from mapnik import (PolygonSymbolizer, LineSymbolizer,
                    Rule, Style, Color,
                    Layer, Shapefile,
                    Map, Image, render)

rule = Rule()
rule.symbols.append(PolygonSymbolizer(Color("grey")))
rule.symbols.append(LineSymbolizer(Color("black"), 0.1))

style = Style()
style.rules.append(rule)

layer = Layer('world')
layer.datasource = Shapefile(file='coastlines/land')
layer.styles.append('world')

m = Map(800, 400)
m.background = Color('white')
m.append_style('world', style)
m.layers.append(layer)

m.zoom_to_box(layer.envelope())
image = Image(800, 400)
render(m, image)
with open('test.png', 'w') as image_file:
    image_file.write(image.tostring('png'))
