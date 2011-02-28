from mapnik import *

rule = Rule()
rule.symbols.append(PolygonSymbolizer(Color("#f2eff9")))
rule.symbols.append(LineSymbolizer(Color("grey"), 0.1))
style = Style()
style.rules.append(rule)
m = Map(800, 400)
layer = Layer('world')
layer.datasource = Shapefile(file='tile-server/coastlines/110m_land')
layer.styles.append('world')
m.append_style('world', style)
m.layers.append(layer)
m.zoom_to_box(layer.envelope())
print layer.envelope()
image = Image(800, 400)
render(m, image)
with open('test.png', 'w') as map:
    map.write(image.tostring('png8'))
