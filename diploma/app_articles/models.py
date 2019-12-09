from django.db import models

from app_eshop.models import Product, Section


class Article(models.Model):
    section = models.ForeignKey(Section, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.CharField(max_length=128, null=True, blank=True, verbose_name='Изображение')
    products = models.ManyToManyField(Product,  null=True, blank=True, verbose_name='Продукты')
    slug = models.SlugField(max_length=100, null=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title



