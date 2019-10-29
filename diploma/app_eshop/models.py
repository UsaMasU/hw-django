from django.db import models


class Phone(models.Model):
    STATUS_CHOICE = (
                    ('available', 'Available'),
                    ('not available', 'Not available'),
                    ('awaiting delivery', 'Awaiting delivery'),
                    ('discontinued', 'Discontinued')
                    )
    id = models.AutoField(verbose_name='ID', primary_key=True)
    name = models.CharField(verbose_name='Name', max_length=30)
    price = models.CharField(verbose_name='Price', max_length=10)
    qty = models.CharField(verbose_name='Quantity', max_length=10)
    image = models.CharField(verbose_name='Image', max_length=128)
    release_date = models.DateField(verbose_name='Release date')
    status = models.CharField(max_length=30, choices=STATUS_CHOICE, default='available')
    slug = models.SlugField(max_length=100)

    class Meta:
        verbose_name = 'Смартфон'
        verbose_name_plural = 'Смартфоны'

    def __str__(self):
        return self.name
