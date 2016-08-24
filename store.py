#!/usr/bin/python2.7
import json
import sense
import sqlite3
import time


#connect to database pi.db
conn = sqlite3.connect('pi.db')
c = conn.cursor()

#Create table
#c.execute('''CREATE TABLE atmos_data
#             (epoch integer, temperature real, pressure real, humidity real)''')
#c.execute('''CREATE TABLE accel_data
#             (epoch integer, x real, y real, z real)''')
#c.execute('''CREATE TABLE ori_data
#             (epoch integer, pitch real, yaw real, roll real)''')

while True:

    #Getting data in json format and parsing it
    get_json = sense.get_sense()
    data = json.loads(get_json)

    #insert a row of atmos_data
    query_atmos = "insert into atmos_data values (?,?,?,?)"
    keys_atmos = data["epoch"],data["temperature"],data["pressure"],data["humidity"]
    c.execute(query_atmos,keys_atmos)

    #insert a row of accel_data
    query_accel = "insert into accel_data values (?,?,?,?)"
    keys_accel = data["epoch"],data["acceleration"]["x"],data["acceleration"]["y"],data["acceleration"]["z"]
    c.execute(query_accel,keys_accel)

    #insert a row of ori_data
    query_ori = "insert into ori_data values (?,?,?,?)"
    keys_ori = data["epoch"],data["orientation"]["pitch"],data["orientation"]["yaw"],data["orientation"]["roll"]
    c.execute(query_ori,keys_ori)
  
    #commit changes
    conn.commit()
    time.sleep(1)

#Close the connection
conn.close()
