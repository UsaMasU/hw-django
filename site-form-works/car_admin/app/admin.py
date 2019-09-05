from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):

    list_display = ('model', 'brand', 'review_count')
    list_filter = ('model', 'brand',)


class CarInline(admin.StackedInline):
    model = Car
    extra = 0
    ordering = ('-id',)


class ReviewAdmin(admin.ModelAdmin):
    form = ReviewAdminForm


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
