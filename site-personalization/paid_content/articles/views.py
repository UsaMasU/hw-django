from django.shortcuts import render
from .models import Article


def show_articles(request):
    return render(
        request,
        'articles.html'
    )


def show_article(request, id):
    article = Article.objects.get(id=id)

    context = {
        'title': article.title,
        'text': article.text
    }
    return render(request, 'article.html', context)
