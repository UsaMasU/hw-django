from django.views.generic import ListView
from django.shortcuts import render

from .models import Article


def articles_list(request):

    template_name = 'articles/news.html'
    object_topics = []
    genre_items = {}
    author_items = {}

    author = request.GET.get('author')
    genre = request.GET.get('genre')

    if author != None:
        object_list = Article.objects.all().select_related('author').filter(author__name=author)
    elif genre != None:
        object_list = Article.objects.all().select_related('genre').filter(genre__name=genre)
    else:
        object_list = Article.objects.order_by('-published_at')[:3]

    topics = Article.objects.select_related('author').select_related('genre').defer(
        'title',
        'text',
        'published_at',
        'image',
    )

    for topic in topics:
        genre_items[topic.genre.name] = topic.genre.name
        author_items[topic.author.name] = topic.author.name

    for genre in genre_items:
        genre_obj = {
            'genre': genre
        }
        object_topics.append(genre_obj)

    for author in author_items:
        author_obj = {
            'author': author
        }
        object_topics.append(author_obj)

    context = {
        'object_list': object_list,
        'topics': object_topics
    }

    return render(request, template_name, context)
