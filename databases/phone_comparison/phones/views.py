from django.shortcuts import render
from .models import Phone, IphoneSE


def show_catalog(request):
    template = 'catalog.html'
    context = {}
    #Person.objects.all().select_related('car')
    phone = Phone.objects.all()
    iphone = IphoneSE.objects.all()
    print(phone[0].name)
    print(len(iphone))
    return render(
        request,
        template,
        context
    )
