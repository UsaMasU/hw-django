from django.shortcuts import render
from .models import Player, Game, PlayerGameInfo

import random


def show_home(request):
    number = -1
    if request.method == 'POST':
        number = request.POST.get("enter_number")
        number = int(number)

    if request.session.has_key('x_number_game'):
        session_data = request.session.get('x_number_game')
        game = Game.objects.get(id=session_data['game_id'])
        player_game_info = PlayerGameInfo.objects.get(game_id=session_data['game_id'])

        if game.state == 'game over':
            del request.session['x_number_game']
            text = f'ваше число: {str(game.x_number)} угадали с {str(player_game_info.attempts)} попыток'
            context = {
                'text': text
            }
            return render(request, 'home.html', context)
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
                    text = 'Загаданное число Меньше. Угадайте число:'
                elif number < x_number:
                    text = 'Загаданное число Больше. Угадайте число:'
                else:
                    text = 'ДА!'
                    role = 'winner'
                    game = Game.objects.get(id=game_id)
                    game.state = 'game over'
                    game.save()
                    request.session['x_number_game']['game_state'] = 'game over'
            request.session['x_number_game']['attempts'] = attempts
            player_game_info = PlayerGameInfo.objects.get(game_id=session_data['game_id'])
            player_game_info.attempts = attempts
            player_game_info.save()
            request.session.modified = True
            context = {
                'role': role,
                'text': text,
                'attempts': attempts,
                'x_number': x_number
            }
            return render(request, 'home.html', context)
        else:
            text = f'Число {str(game.x_number)} сейчас пытаются угадать'
            context = {
                'role': role,
                'text': text,
                'x_number': x_number
            }
            return render(request, 'home.html', context)
    else:
        games = Game.objects.all()
        if len(games) > 0:
            for game in games:
                if game.state == 'playing':
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
                    request.session['x_number_game'] = game_data
                    text = 'Угадайте число'
                    context = {
                        'role': role,
                        'text': text,
                        'x_number': game.x_number
                    }
                    return render(request, 'home.html', context)

        player = Player(name='Player_Creator')
        player.save()
        x_number = random.randint(0, 100)
        game = Game(x_number=x_number, state='playing')
        game.save()
        player_game_info = PlayerGameInfo.objects.create(player=player, game=game, attempts=0)
        role = 'creator'
        game_data = {
            'player_id': player.id,
            'role' : role,
            'game_id': game.id,
            'game_state': game.state,
            'game_x_number': x_number,
            'attempts': 0
        }
        request.session['x_number_game'] = game_data

        text = f'Начинаем игру. Загаданное число: {str(game.x_number)}'
        context = {
            'role': role,
            'text': text,
            'x_number': x_number
        }
        return render(request, 'home.html', context)
