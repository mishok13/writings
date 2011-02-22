from mapnik import (Map, Image, Envelope, render, Rule, Color,
                    Layer, Shapefile,
                    Style, PolygonSymbolizer, LineSymbolizer)


def create_style(rule):
    rule = Rule()
    rule.symbols.append(PolygonSymbolizer(Color("#f2eff9")))
    rule.symbols.append(LineSymbolizer(Color("black"), 0.1))
    style = Style()
    style.rules.append(rule)
    return style


def create_layer(style_name):
    layer = Layer('world')
    layer.datasource = Shapefile(file='path/to/shapefile')
    layer.styles.append(style_name)
    return layer


def create_map():
    m = Map(800, 400)
    m.append_style('base', create_style)


m = Map(800, 400)
m.append_style(style)
m.layers.append(layer)
m.zoom_to_box(layer.envelope())
image = Image(800, 400)
render(m, image)
image.tostring('png8')
