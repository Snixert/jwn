#!/usr/bin/env python3

from flask import Flask
from sense_hat import SenseHat
hat = SenseHat()
app = Flask(__name__)

@app.get('/temperature')
def list_programming_languages():
   return {"programming_languages":list(in_memory_datastore.values())}