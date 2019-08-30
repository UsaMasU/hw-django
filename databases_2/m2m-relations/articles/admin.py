from django.contrib import admin

from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Topic, Relationship


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        base_status_count = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить

            if(form.cleaned_data.get('base_status')):
                base_status_count += 1

            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
        if (base_status_count == 0):
            raise ValidationError('Укажите основной раздел')
        if(base_status_count > 1):
            raise ValidationError('Основным может быть только один радел')
        return super().clean()  # вызываем базовый код переопределяемого метода


class RelationshipInline(admin.TabularInline):
    model = Relationship
    formset = RelationshipInlineFormset
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    inlines = (RelationshipInline,)


class TopicAdmin(admin.ModelAdmin):
    inlines = (RelationshipInline,)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Topic, TopicAdmin)
