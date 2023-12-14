from ip2geotools.databases.noncommercial import DbIpCity
import geocoder
import csv
import folium
import pandas as pd
import folium.plugins as plugins
from folium.plugins import MarkerCluster

def csv_maker(file):
    dictionary_counter={}
    dictionary_ips_all_info={}
    for ip in file:
        try:
            g=geocoder.ip(str(ip))
            latitude = g.lat
            longtitude=g.lng
            if ip not in dictionary_counter:
                dictionary_ips_all_info[ip]= [g.address, g.lat, g.lng, 1]
                dictionary_counter[ip]=1
            else:
                dictionary_counter[ip]+=1
                dictionary_ips_all_info[ip]= [g.address, g.lat, g.lng, dictionary_counter[ip]]
        except:
            print(ip+" is not valid")
    with open("IPs_INFO.csv", "a") as fp:
        wr = csv.writer(fp, dialect='excel')
        wr.writerow(("IP","Location", "Latitude", "Longitude", "Count"))
        for key in dictionary_ips_all_info.keys():
            wr.writerow([key]+ dictionary_ips_all_info[key])

def map():
    df = pd.read_csv('IPs_INFO.csv')
    locs = df[["Latitude", "Longitude"]].values.tolist()
    pops = df[["IP", "Location", "Latitude", "Longitude"]].values.tolist()
    m = folium.Map([42.363,-71.0995],zoom_start=3)
    MarkerCluster(locations=locs, popups=pops).add_to(m)
    m.save("MAP_output.html")

def main():
    f=open("ip-list.txt", "r")
    csv_maker(f)  

main()
map()
