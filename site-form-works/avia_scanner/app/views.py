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
    results = []

    if cache.get('cities') is None:
        cities = City.objects.all()
        for city in cities:
            results.append(city.name)
        cache.set('cities', results, 30)
    else:
        results = cache.get('cities')

    return JsonResponse(results, safe=False)
