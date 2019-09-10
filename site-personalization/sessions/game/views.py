from django.shortcuts import render
from .models import Player, Game, PlayerGameInfo

from django.http import HttpResponseRedirect
from django.urls import reverse

import random


def show_home(request):
    number = -1
    #del  request.session['x_number_game']
    #return False

    if request.method == 'POST':
        number = request.POST.get("enter_number")
        number = int(number)
        print('entered number:', number)

    if request.session.has_key('x_number_game'):
        session_data = request.session.get('x_number_game')
        print('active session:', session_data)
        game_state = session_data['game_state']
        player_id = session_data['player_id']
        game_id = session_data['game_id']
        x_number = session_data['game_x_number']
        attempts = session_data['attempts']
        role = session_data['role']
        text = 'Угадайте число:'
        x_number = int(x_number)

        if role == 'finder':
            if number is not -1:
                attempts += 1
                if number > x_number:
                    print('Больше')
                    text = 'Загаданное число Меньше. Угадайте число:'
                elif number < x_number:
                    print('Меньше')
                    text = 'Загаданное число Больше. Угадайте число:'
                else:
                    print('Рввно')
                    text = 'ДА!'
                    role = 'winner'
                    game = Game.objects.get(id=game_id)
                    game.state = 'over'
                    game.save()
                    game_state = game.state
                    request.session['x_number_game']['game_state'] = game.state

            print('state', game_state)
            if game_state == 'playing':
                print('yes - playing')
                request.session['x_number_game']['attempts'] = attempts
                request.session.modified = True
            else:
                del request.session['x_number_game']
                #return HttpResponseRedirect(reverse('home'))

            context = {
                'role': role,
                'text': text,
                'attempts': attempts,
                'x_number': x_number
            }
            return render(request, 'home.html', context)
        else:
            text = 'Ваше число разгадывают'
            context = {
                'role': role,
                'text': text,
                'x_number': x_number
            }
            return render(request, 'home.html', context)
    else:
        print('no session')
        games = Game.objects.all()
        print(games)

        if len(games) > 0:
            for game in games:
                print('game:', game.state)
                if game.state == 'playing':
                    print('active game:', game.id)
                    print('x:', game.x_number)
                    print('state:', game.state)

                    player = Player(name='Player_Finder')
                    player.save()
                    role = 'finder'

                    game_data = {
                        'player_id': player.id,
                        'role': role,
                        'game_id': game.id,
                        'game_state': game.state,
                        'game_x_number': game.x_number,
                        'attempts': 0
                    }
                    print(game_data)
                    request.session['x_number_game'] = game_data

                    text = 'Угадайте число'
                    context = {
                        'role': role,
                        'text': text,
                        'x_number': game.x_number
                    }
                    return render(request, 'home.html', context)

        print('no active game')
        player = Player(name='Player_Creator')
        player.save()
        x_number = random.randint(0, 100)
        game = Game(x_number=x_number, state='playing')
        game.save()
        player_game_info = PlayerGameInfo.objects.create(player=player, game=game, attempts=0)
        print(player_game_info)

        print('player:', player.id)
        print('game:', game.id)
        print('player_game_info:', player_game_info.id)
        role = 'creator'

        game_data = {
            'player_id': player.id,
            'role' : role,
            'game_id': game.id,
            'game_state': game.state,
            'game_x_number': x_number,
            'attempts': 0
        }
        print(game_data)
        request.session['x_number_game'] = game_data

        text = 'Начинаем игру'
        context = {
            'role': role,
            'text': text,
            'x_number': x_number
        }
        return render(request, 'home.html', context)
