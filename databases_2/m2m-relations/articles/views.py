from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Relationship
from pprint import pprint


def articles_list(request):
    template = 'articles/news.html'

    relationships = Relationship.objects.all()

    object_list = []
    same_article = False
    for article in relationships:
        for item in object_list:
            if article.article.id == item['id']:
                same_article = True
        if same_article:
            object_list[-1]['scopes'].append({
                'topic': article.topic,
                'is_main': article.base_status
            })
            same_article = False
            continue
        object_list.append({
            'id': article.article.id,
            'title': article.article.title,
            'text': article.article.text,
            'image': article.article.image,
            'scopes': [{
                'topic': article.topic,
                'is_main': article.base_status
            }]
        })
    pprint(object_list)

    context = {
        'object_list': object_list,
    }

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)
