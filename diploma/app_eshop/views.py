from django.shortcuts import render

from app_eshop.models import Phone


def main(request):
    print('_main page')
    template_name = 'app_eshop/index.html'
    context = {}
    return render(request, template_name, context)

def phones(request):
    print('_main page')
    template_name = 'app_eshop/smartphones.html'
    context = {}
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
