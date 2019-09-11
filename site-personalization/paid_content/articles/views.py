from django.shortcuts import render, redirect
from .models import Article, Profile
from django.contrib.auth.decorators import login_required


@login_required
def show_articles(request):
    user = request.user
    vip_status = False
    articles= Article.objects.only('id')
    profiles = Profile.objects.only('vip_access')
    articles_show = []

    for profile in profiles:
        if user == profile.vip_access:
            vip_status = True
            break

    if vip_status:
        articles_show = articles
        access_type = 'VIP'
    else:
        access_type = 'Standart'
        for article in articles:
            if not article.vip:
                articles_show.append(article)

    context = {
        'articles': articles_show,
        'access_type': access_type
    }
    return render(request, 'articles.html', context)


@login_required
def show_article(request, id):
    article = Article.objects.get(id=id)

    context = {
        'title': article.title,
        'text': article.text,
        'vip': article.vip
    }
    return render(request, 'article.html', context)


def subscribe_control(request):
    user = request.user
    if request.method == 'POST':
        try:
            user_profile = Profile.objects.get(vip_access=user)
            user_profile.delete()
        except:
            user_profile = Profile(vip_access=user)
            user_profile.save()
        return redirect('main')



    articles = Article.objects.only('id')

    context = {
        'articles': articles
    }
    return render(request, 'subscribe.html', context)