layer = Layer('continents')
layer.datasource = Shapefile(
    file='coastlines/land')
layer.styles.append('world-style')
