#!/usr/bin/env python3

from flask import Flask, jsonify
from sense_hat import SenseHat
from hello_sense import run
hat = SenseHat()
app = Flask(__name__)

run()

@app.get('/temp')
def getTemperature():
   temp = hat.get_temperature()
   return jsonify({'temperature':temp})

@app.get('/humidity')
def getHumidity():
   humidity = hat.get_humidity()
   return jsonify({'temperature':humidity})