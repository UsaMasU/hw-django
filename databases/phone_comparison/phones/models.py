from django.db import models


class Phone(models.Model):
    cost = models.TextField()
    name = models.TextField()
    size = models.TextField()
    os = models.TextField()
    ram = models.TextField()
    color = models.TextField()
    accum = models.TextField()
    cam_dpi = models.TextField()


class IphoneSE(models.Model):
    cost = models.TextField()
    name = models.TextField()
    size = models.TextField()
    os = models.TextField()
    ram = models.TextField()
    color = models.TextField()
    accum = models.TextField()
    cam_dpi = models.TextField()
