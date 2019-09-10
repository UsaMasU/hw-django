from django.shortcuts import render
import random


def show_home(request):

    x_number = random.randint(0, 100)

    my_car = request.session.get('x_number_game', 'start')

    return render(
        request,
        'home.html'
    )
