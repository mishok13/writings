layer = Layer('world')
layer.datasource = Shapefile(file='coastlines/land')
layer.styles.append('world')
