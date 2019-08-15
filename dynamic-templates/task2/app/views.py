from django.shortcuts import render

#view_act = 'active'

def home_view(request):
    template_name = 'app/home.html'
    context = {
        'view_name': 'home'
    }
    return render(request, template_name, context)


def about_view(request):
    template_name = 'app/about.html'
    context = {
        'view_name': 'about'
    }
    return render(request, template_name, context)


def contacts_view(request):
    template_name = 'app/contacts.html'
    context = {
        'view_name': 'contacts'
    }
    return render(request, template_name, context)


def examples_view(request):
    template_name = 'app/examples.html'

    items = [{
        'title': 'Apple II',
        'text': 'Легенда',
        'img': 'ii.jpg'
    }, {
        'title': 'Macintosh',
        'text': 'Свежие новинки октября 1983-го',
        'img': 'mac.jpg'
    }, {
        'title': 'iMac',
        'text': 'Оригинальный и прозрачный',
        'img': 'imac.jpg'
    }]
    context = {
        'items': items,
        'view_name': 'examples'
    }
    return render(request, template_name, context)
