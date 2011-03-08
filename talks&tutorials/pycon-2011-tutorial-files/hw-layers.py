layer = Layer('coastlines')
layer.datasource = Shapefile(
    file='coastlines/land')
layer.styles.append('landmass')
