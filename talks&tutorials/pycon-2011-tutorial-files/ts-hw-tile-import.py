from flask import Flask, Response
from utils import render, parse_coords
import mapnik

map = mapnik.Map(0, 0)
mapnik.load_map(map, "map.xml")
app = Flask(__name__)
