#!/usr/bin/python2.7
import json
import time
from sense_hat import SenseHat

def get_sense():
    sense = SenseHat()
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()
    orientation = sense.get_orientation()
    acceleration = sense.get_accelerometer_raw()
    epoch = time.time()
    #consctruct the json string
    data = {}
    data['epoch'] = epoch
    data['temperature'] = t
    data['pressure'] = p
    data['humidity'] = h
    data['orientation'] = orientation
    data['acceleration'] = acceleration
    json_data = json.dumps(data)
    return json_data
