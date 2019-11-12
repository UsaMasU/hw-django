from django.db import models


class Product(models.Model):
    STATUS_CHOICE = (
                    ('available', 'Available'),
                    ('not available', 'Not available'),
                    ('awaiting delivery', 'Awaiting delivery'),
                    ('discontinued', 'Discontinued')
                    )
    SECTIONS = (
        ('---', '---'),
        ('miscellaneous', 'Miscellaneous'),
        ('smartphones', 'Smartphones'),
        ('accessories', 'Accessories'),
        ('cultural', 'Cultural')
    )
    id = models.AutoField(verbose_name='ID', primary_key=True)
    section = models.CharField(max_length=30, choices=SECTIONS, default='---')
    name = models.CharField(verbose_name='Name', max_length=30)
    price = models.CharField(verbose_name='Price', max_length=10)
    qty = models.CharField(verbose_name='Quantity', max_length=10)
    image = models.CharField(verbose_name='Image', max_length=128)
    release_date = models.DateField(verbose_name='Release date')
    status = models.CharField(max_length=30, choices=STATUS_CHOICE, default='available')
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class Review(models.Model):
    RATING_CHOICE = (
       ('★', '★'),
       ('★★', '★★'),
       ('★★★', '★★★'),
       ('★★★★', '★★★★'),
       ('★★★★★', '★★★★★')
    )
    publish_date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Author\'s name', max_length=30)
    text = models.TextField(verbose_name='Review text', max_length=255)
    rating = models.CharField(max_length=30, choices=RATING_CHOICE, default='★')

    def __str__(self):
        return str(self.product.name) + ' ' + self.text[:50]


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.CharField(verbose_name='Price', max_length=10)
    qty = models.CharField(verbose_name='Quantity', max_length=10)
    user_id = models.CharField(verbose_name='User id', max_length=255)

    def __str__(self):
        return self.product
