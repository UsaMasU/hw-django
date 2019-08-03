from django.shortcuts import render_to_response, redirect
from django.urls import reverse

from app.settings import BUS_STATION_CSV
import csv

import urllib.parse

bus_stations_data = []
prev_page = '?' + urllib.parse.urlencode({'page': 1})
next_page = '?' + urllib.parse.urlencode({'page': 2})

def index(request):
    with open(BUS_STATION_CSV, encoding='cp1251', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            bus_stations_data.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})
    return redirect(reverse(bus_stations))


def bus_stations(request):
    bus_stations_show = []
    stations_quant = len(bus_stations_data)
    page_number = request.GET.get('page')

    if(page_number == '1') or (page_number == None):
        station_start = 0
        station_end = round(stations_quant / 2)
    if(page_number == '2'):
        station_start = round(stations_quant / 2)
        station_end = stations_quant

    for item_num in range(station_start, station_end):
        bus_stations_show.append(bus_stations_data[item_num])

    return render_to_response('index.html', context={
        'bus_stations':  bus_stations_show,
        'current_page': 1,
        'prev_page_url': prev_page,# None
        'next_page_url': next_page # 'bus_stations/?page=2'
    })

