from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    vip_access = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='VIP')


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    vip = models.BooleanField(default=False,verbose_name='VIP')

    def __str__(self):
        return f'{self.title}'
