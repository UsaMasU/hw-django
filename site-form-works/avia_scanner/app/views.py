import time
import random

from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache

from .models import City
from .forms import SearchTicket


def ticket_page_view(request):
    template = 'app/ticket_page.html'

    context = {
        'form': SearchTicket()
    }

    return render(request, template, context)


def cities_lookup(request):
    """Ajax request предлагающий города для автоподстановки, возвращает JSON"""
    cache_list = cache.get('cities', [])
    match_selected = []

    if cache.get('cities') is None:
        cities = City.objects.all()
        for city in cities:
            cache_list.append(city.name)
        cache.set('cities', cache_list, 30)

    get_input = request.GET

    for city in cache_list:
        if get_input['term'].lower() in city.lower()[0:5]:
            match_selected.append(city)

    results = match_selected if len(match_selected) > 0 else cache_list

    return JsonResponse(results, safe=False)
