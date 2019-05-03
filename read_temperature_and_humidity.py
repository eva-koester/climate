#!/usr/bin/python
import sys
import Adafruit_DHT

sensor=11
pin=4

while True:
    humidity, temperature=Adafruit_DHT.read_retry(sensor, pin)
    print('Temp:{0:0.1f} C Humidity:{1:0.1f}'.format(temperature,humidity))

    with open("log.csv", "at") as logfile:
        logfile.write("{0:0.2f},{1:0.2f}\n".format(temperature, humidity))

