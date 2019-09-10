from django.shortcuts import render
from .models import Player, Game, PlayerGameInfo

import random


def show_home(request):
    # if request.session.has_key('x_number_game'):
    #     del request.session['x_number_game']
    #     return render(request, 'home.html')
    my_game = request.session.get('x_number_game')
    print('session:', my_game)

    # game_data2 = {
    #     'player_id': 5,
    #     'game_id': 1,
    #     'game_attempts': 0,
    #     'game_state': 'playing'
    # }
    # print(game_data2)
    # request.session['x_number_game2'] = game_data2  # game.id

    game_data2 = request.session.get('x_number_game2')
    print('w', game_data2)

    if request.session.has_key('x_number_game'):
        game_id = request.session.get('x_number_game')
        print('active session:', game_id)

        game = Game.objects.get(id=game_id)
        print('x number:', game.x_number)
        text = 'Угадайте число:'
        context = {
            'text': text,
            'x_number': game.x_number
        }

        if game.state == 'over':
            del request.session['x_number_game']

        return render(request, 'home.html', context)
    else:
        print('no session')
        games = Game.objects.all()
        print(games)

        for game in games:
            print('game:', game.state)
            if game.state == 'playing':
                print('active game:', game.id)
                print('x:', game.x_number)
                print('state:', game.state)

                text = 'Угадайте число'
                context = {
                    'text': text,
                    'x_number': game.x_number
                }
                return render(request, 'home.html', context)

        print('no active game')
        player = Player(name='Player')
        player.save()
        x_number = random.randint(0, 100)
        game = Game(x_number=x_number, state='playing')
        game.save()
        player_game_info = PlayerGameInfo.objects.create(player=player, game=game, attempts=0)
        print(player_game_info)

        print('player:', player.id)
        print('game:', game.id)
        print('player_game_info:', player_game_info.id)

        game_data = {
            'player_id': player.id,
            'game_id': game.id,
            'game_attempts': player_game_info.attempts,
            'game_state': game.state
        }
        print(game_data)
        request.session['x_number_game'] = game_data  # game.id
        text = 'Начинаем игру'
        context = {
            'text': text,
            'x_number': x_number
        }
        return render(request, 'home.html', context)

    #    my_game = request.session.get('x_number_game', 'start')
