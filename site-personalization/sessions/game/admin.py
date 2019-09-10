from django.contrib import admin
from .models import Player, Game, PlayerGameInfo

from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


class PlayerGameInfoInlineFormset(BaseInlineFormSet):
    def clean(self):
        return super().clean()


class PlayerGameInfoInline(admin.TabularInline):
    model = PlayerGameInfo
    formset = PlayerGameInfoInlineFormset
    extra = 1


class PlayerAdmin(admin.ModelAdmin):
    inlines = (PlayerGameInfoInline,)


class GameAdmin(admin.ModelAdmin):
    pass


admin.site.register(Player, PlayerAdmin)
admin.site.register(Game, GameAdmin)
