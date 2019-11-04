from django.contrib import admin
from .models import Phone, Review

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'qty', 'release_date', 'status', 'id')
    list_filter = ('status', 'name', 'release_date')
    search_fields = ('name', 'id')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name', 'id')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
