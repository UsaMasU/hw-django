import urllib.parse

from django.core.paginator import Paginator
from django.shortcuts import render, redirect, render_to_response
from django.urls import reverse

from .models import Phone  # app_eshop

objects_to_page = 3


def index(request):
    return redirect(reverse(main))


def main(request):
    template_name = 'app_eshop/index.html'
    phones = Phone.objects.order_by("-id")[0:3]
    context = {'phones': phones}
    return render(request, template_name, context)


def phones(request):
    template_name = 'app_eshop/smartphones.html'

    phones = Phone.objects.order_by("id")

    page_number = request.GET.get('page')
    paginator = Paginator(phones, objects_to_page)
    page_object = paginator.get_page(page_number)
    phones_show = paginator.page(page_object.number).object_list

    if page_object.has_next():
        next_page = '?' + urllib.parse.urlencode({'page': page_object.next_page_number()})
    else:
        next_page = ''
    if page_object.has_previous():
        prev_page = '?' + urllib.parse.urlencode({'page': page_object.previous_page_number()})
    else:
        prev_page = ''

    return render_to_response(template_name, context={
        'phones': phones_show,
        'current_page': page_object.number,
        'prev_page_url': prev_page,
        'next_page_url': next_page,
        'num_pages': list(range(1, paginator.num_pages+1))
    })


def phone(request, slug):
    template = 'app_eshop/phone.html'
    context = {
        'phone': Phone.objects.get(slug=slug)
    }
    return render(request, template, context)


def accessories(request):
    template_name = 'app_eshop/accessories.html'
    context = {}
    return render(request, template_name, context)


def cart(request):
    template = 'app_eshop/cart.html'
    context = {
    }
    return render(request, template, context)


def login(request):
    template_name = 'login.html'
    context = {}
    return render(request, template_name, context)