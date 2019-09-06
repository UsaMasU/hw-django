from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    pass


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')

    def __str__(self):
        return f'{self.title}'
