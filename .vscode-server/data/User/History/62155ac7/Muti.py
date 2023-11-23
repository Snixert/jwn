#!/usr/bin/env python3

from flask import Flask, jsonify
from sense_hat import SenseHat
hat = SenseHat()
app = Flask(__name__)

@app.get('/temp')
def getTemperature():
   temp = hat.get_temperature()
   return jsonify({'temperature':temp})