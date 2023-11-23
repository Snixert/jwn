#!/usr/bin/env python3

from flask import Flask
from sense_hat import SenseHat
hat = SenseHat()
app = Flask(__name__)

@app.get('/temperature')
def list_programming_languages():
   temp = hat.get_temperature()
   return jsonify('temperature':temp)