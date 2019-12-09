from django.shortcuts import render


def article_show(request, slug):
    template = 'app_articles/article.html'

    article = Article.objects.all().get(slug=slug)
    context = {
        'article': article
    }
    return render(request, template, context)
