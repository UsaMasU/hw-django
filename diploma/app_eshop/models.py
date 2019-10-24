from django.db import models

class Phone(models.Model):
    STATUS_CHOICE = (
                    ('available','Available'),
                    ('not available', 'Not available'),
                    ('awaiting delivery','Awaiting delivery')
                    )
    id = models.CharField(verbose_name = 'ID',  max_length = 30, primary_key=True)
    name = models.CharField(verbose_name = 'Name', max_length = 30)
    price = models.CharField(verbose_name = 'Price', max_length = 10)
    image = models.CharField(verbose_name = 'Image', max_length = 128)
    release_date = models.DateField(verbose_name = 'Release date', auto_now_add = True)
    satus = models.CharField(max_length=10, choices=STATUS_CHOICE, default='available')
    slug = models.SlugField(max_length = 100)
