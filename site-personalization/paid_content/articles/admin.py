from django.contrib import admin
from .models import Profile, Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'vip',)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('vip_access',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Profile, ProfileAdmin)
