from django.contrib import admin
from .models import Phone, IphoneSE


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    pass


class IphoneSEAdmin(admin.ModelAdmin):
    pass


admin.site.register(IphoneSE, IphoneSEAdmin)
