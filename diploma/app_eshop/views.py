

from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Phone   # app_eshop


def index(request):
    print('index:', request)
    return redirect(reverse(main))


def main(request):
    template_name = 'app_eshop/index.html'
    phones = Phone.objects.order_by("-id")[0:3]
    context = {'phones': phones}
    return render(request, template_name, context)


def phones(request):
    template_name = 'app_eshop/smartphones.html'
    phones = Phone.objects.order_by("id")
    context = {'phones': phones}
    return render(request, template_name, context)


def phone(request, slug):
    template = 'product.html'
    context = {
        'phone': Phone.objects.get(slug=slug)
    }
    return render(request, template, context)


def login(request):
    template_name = 'login.html'
    context = {}
    return render(request, template_name, context)
