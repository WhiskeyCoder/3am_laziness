import time
import ip2geotools
import csv

csv_file = 'assets.csv'

with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        ip = row[0]
        try:
            time.sleep(2)
            ip_address = ip2geotools.IPAddress(ip)
            lat = ip_address.latitude
            long = ip_address.longitude
            row.append(lat)
            row.append(long)
            print(row)
        except:
            print("Error")
            row.append(None)
            row.append(None)
            print(row)

with open(csv_file, 'w') as f:
    writer = csv.writer(f)
    writer.writerows(reader)
