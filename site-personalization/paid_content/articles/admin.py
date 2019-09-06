from django.contrib import admin
from .models import Profile, Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title',)


class ProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Article, ArticleAdmin)
admin.site.register(Profile, ProfileAdmin)
