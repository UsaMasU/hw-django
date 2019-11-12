from django.contrib import admin
from .models import Product, Review


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'section', 'price', 'qty', 'release_date', 'status', 'id')
    list_filter = ('section', 'status', 'name', 'release_date')
    search_fields = ('name', 'id')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name', 'id')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
