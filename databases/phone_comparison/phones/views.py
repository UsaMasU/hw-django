from django.shortcuts import render
from .models import Phone, IphoneSE, Asus, Xiaomi


def show_catalog(request):
    template = 'catalog.html'

    phones = []

    phones.append(Phone.objects.all()[0])
    phones.append(IphoneSE.objects.all()[0])
    phones.append(Asus.objects.all()[0])
    phones.append(Xiaomi.objects.all()[0])

    context = {
        'phones': phones
    }

    return render(
        request,
        template,
        context
    )
