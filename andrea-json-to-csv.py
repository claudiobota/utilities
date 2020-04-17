import json
import csv

data_parsed = json.loads(open('data.json', 'r'))
data = open('data.csv', 'w')
csv_writer = csv.writer(data)

for i in range(len(data_parsed)):
    line = data_parsed[i]
    if i == 0:
        csv_writer.writerow(line.keys())
    csv_writer.writerow(line.values())
    
data.close()
