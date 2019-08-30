from django.views.generic import ListView
from django.shortcuts import render

from .models import Article


def articles_list(request):
    template_name = 'articles/news.html'
    object_list = []

    # items = Article.objects.defer('genre')
    # items = Article.objects.all()

    #items = Article.objects.get(author_id=3)

    items = Article.objects.select_related('author').select_related('genre').defer(
        'title',
        'text',
        'published_at',
        'image',
    )

    print(items)

    # "articles_article".
    # "author_id",
    # "articles_article".
    # "genre_id",
    # "articles_article".
    # "title",
    # "articles_article".
    # "text",
    # "articles_article".
    # "published_at",
    # "articles_article".
    # "image",
    # "articles_author".
    # "id",
    # "articles_author".
    # "name",
    # "articles_author".
    # "phone",
    # "articles_genre".
    # "id",
    # "articles_genre".
    # "name"

    for item in items:
        print(item.author.name)
        print(item.genre.name)

    # object_list = articles
    context = {
        'object_list': object_list,
    }

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template_name, context)
