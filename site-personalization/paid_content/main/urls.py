"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

import django.contrib.auth

from articles.views import show_articles, show_article, subscribe_control

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_articles,name='main'),
    path('articles/', show_articles),
    path('subscribe/', subscribe_control),
    url(r'^articles/(?P<id>[0-9]+)/', show_article),
]

urlpatterns += [
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
