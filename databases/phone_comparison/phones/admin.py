from django.contrib import admin
from .models import Phone, IphoneSE, Asus, Xiaomi


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    pass


class IphoneSEAdmin(admin.ModelAdmin):
    pass


class AsusAdmin(admin.ModelAdmin):
    pass


class XiaomiAdmin(admin.ModelAdmin):
    pass


admin.site.register(IphoneSE, IphoneSEAdmin)
admin.site.register(Asus, AsusAdmin)
admin.site.register(Xiaomi, XiaomiAdmin)
