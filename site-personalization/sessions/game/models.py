from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')

    def __str__(self):
        return self.name


class Game(models.Model):
    x_number = models.IntegerField(default=0)
    state = models.CharField(max_length=20, verbose_name='Статус игры')
    players = models.ManyToManyField(Player, through='PlayerGameInfo', verbose_name='Игроки')

    def __str__(self):
        return self.state


class PlayerGameInfo(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, verbose_name='Игрок')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Игра')
    attempts = models.IntegerField(default=0)

    def __str__(self):
        return '{0}_{1}'.format(self.player, self.game)
