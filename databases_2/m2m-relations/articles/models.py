from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
       verbose_name = 'Статья'
       verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Topic(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    articles = models.ManyToManyField(Article, through='Relationship', verbose_name='статьи')

    class Meta:
       verbose_name = 'Тематический раздел'
       verbose_name_plural = 'Тематические разделы'

    def __str__(self):
        return self.name

class Relationship(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='статья')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='тематический раздел')
    base_status = models.BooleanField(verbose_name='Основной')

    class Meta:
       verbose_name = 'Связанные темы'
       verbose_name_plural = 'Связанные темы'

    def __str__(self):
        return '{0}_{1}'.format(self.article, self.topic)
