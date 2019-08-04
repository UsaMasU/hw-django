from django.shortcuts import render_to_response, redirect
from django.urls import reverse

from django.core.paginator import Paginator
from app.settings import BUS_STATION_CSV
import csv

import urllib.parse

bus_stations_data = []
objects_to_page = 10

def index(request):
    with open(BUS_STATION_CSV, encoding='cp1251', newline='') as file_csv:
        reader = csv.DictReader(file_csv)
        for row in reader:
            bus_stations_data.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})
    return redirect(reverse(bus_stations))


def bus_stations(request):
    page_number = request.GET.get('page')

    paginator = Paginator(bus_stations_data, objects_to_page)
    page_object = paginator.get_page(page_number)

    print('count objects:', paginator.count)
    print('pages:', paginator.num_pages)
    print('current page:', page_object)

    bus_stations_show = paginator.page(page_object.number).object_list
    print('page objects to show:', bus_stations_show)

    if(page_object.has_next()):
        next_page = '?' + urllib.parse.urlencode({'page':page_object.next_page_number()})
    else:
        next_page = ''

    if (page_object.has_previous()):
        prev_page = '?' + urllib.parse.urlencode({'page': page_object.previous_page_number()})
    else:
        prev_page = ''

    return render_to_response('index.html', context={
        'bus_stations':  bus_stations_show,
        'current_page': page_object.number,
        'prev_page_url': prev_page,
        'next_page_url': next_page
    })

