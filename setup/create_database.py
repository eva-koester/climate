from influxdb import InfluxDBClient

DB = 'climate'
client = InfluxDBClient(host="localhost", port=8086)


all_databases = client.get_list_database()
print(all_databases)

for db in all_databases:
    print(db['name'])
    if db['name'] == DB:
        print('gibt es schon!')
        break
else:
    client.create_database(DB)
