#!/usr/bin/env python3

from flask import Flask, jsonify
from sense_hat import SenseHat
hat = SenseHat()
app = Flask(__name__)

@app.get('/temp')
def getTemperature():
   temp = hat.get_temperature()
   return jsonify({'temperature':temp})

@app.get('/temp')
def getTemperature():
   humidity = hat.get_humidity()
   return jsonify({'temperature':humidity})