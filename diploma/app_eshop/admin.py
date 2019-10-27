from django.contrib import admin
from .models import Phone


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'release_date', 'status', 'id')
    list_filter = ('status', 'name', 'release_date', 'id')
    search_fields = ('name', 'id')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name', 'id')
