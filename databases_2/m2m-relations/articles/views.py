from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, Topic, Relationship
from pprint import pprint

def articles_list(request):
    template = 'articles/news.html'

    topics = []

    news_articles = Article.objects.all()
    news_topics = Topic.objects.all()
    news_relationships = Relationship.objects.all()

    #print('articles: ', news_articles)
    #print('topics: ',news_topics)
    #print('relations: ', news_relationships)
    print('-----------------------')

    #is_main = Relationship.objects.filter(base_status='True')
    #print('mains: ', is_main)

    #rel = Relationship.objects.values()
    #print(rel)

    object_list = []
    for item in news_relationships:
        e = {}
        #print(item.article)
        #print(item.topic)
        e['id'] = item.article.id
        e['title'] = item.article.title
        e['text'] = item.article.text
        e['image'] = item.article.image
        e['scope'] = item.topic.id
        object_list.append(e)

    pprint(object_list)


    #0ss = Topic.objects.all().prefetch_related('articles')
    #print(ss[0][0])

    #print(Article.objects.order_by('topics'))
    #str_main = is_main[0]
    #str_topic = str(str_main).split('_')[1]
    #print(str_topic)
    #print(str(Relationship.objects.filter(base_status='True')[0]).split('_')[1])

    #is_main = str(Relationship.objects.filter(base_status='True')[0]).split('_')[1]
    #print(is_main)




    context = {
        'object_list': object_list #news_articles,
    }

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)
