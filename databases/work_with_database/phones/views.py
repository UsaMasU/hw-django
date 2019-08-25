from django.shortcuts import render
from .models import Phone


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')

    if(sort == 'name'):
        phones = Phone.objects.order_by("name")
    elif(sort == 'min_price'):
        phones = Phone.objects.order_by("-price")
    else:
        phones = Phone.objects.all()

    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        'phone': Phone.objects.get(slug = slug)
    }
    return render(request, template, context)
