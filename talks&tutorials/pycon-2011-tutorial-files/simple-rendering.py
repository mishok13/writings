from mapnik import *

rule = Rule()
rule.symbols.append(PolygonSymbolizer(Color("#f2eff9")))
rule.symbols.append(LineSymbolizer(Color("grey"), 0.1))
style = Style()
style.rules.append(rule)
m = Map(800, 400)
layer = Layer('world')
layer.datasource = Shapefile(file='coastlines/110m_land')
layer.styles.append('world')
m.append_style('world', style)
m.layers.append(layer)
m.zoom_to_box(layer.envelope())
image = Image(800, 400)
render(m, image)
with open('test.png', 'w') as image_file:
    image_file.write(image.tostring('png'))
