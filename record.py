from influxdb import InfluxDBClient

DB = 'climate'

client = InfluxDBClient(host="localhost", port=8086)
client.switch_database(DB)

def write_to_db(temperature, humidity):
    measurement = [{
        'measurement': 'climate',
        'tags': {},
        'fields': {'temperature': temperature, 'humidity': humidity}
    }]
    client.write_points(measurement)
    