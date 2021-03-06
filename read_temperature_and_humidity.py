#!/usr/bin/python
import sys
from record import write_to_db
import Adafruit_DHT
from datetime import datetime

sensor=11
pin=4

while True:
    humidity, temperature=Adafruit_DHT.read_retry(sensor, pin)
    print('Temp:{0:0.1f} C Humidity:{1:0.1f}'.format(temperature,humidity))

    with open("log.csv", "at") as logfile:
        logfile.write("{0:0.2f},{1:0.2f},{2}\n".format(temperature, humidity, str(datetime.now())))
    write_to_db(temperature, humidity)


