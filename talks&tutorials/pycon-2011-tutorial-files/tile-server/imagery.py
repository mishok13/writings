#!/usr/bin/env python


from flask import Flask
import mapnik


app = Flask(__name__)
cache = {}


def render(map, width, height):
    image = mapnik.Image(width, height)
    mapnik.render(map, image)
    return image.tostring('png')


@app.route('/')
def main():
    return 'Hello world'


@app.route('/<int:zoom>/<int:xtile>/<int:ytile>.<image_type>')
def osm_tile(zoom, xtile, ytile, image_type):
    if image_type not in ('png', 'jpg'):
        raise
    print zoom, xtile, ytile, image_type
    return 'fuck yeah'




if __name__ == '__main__':
    app.run()
