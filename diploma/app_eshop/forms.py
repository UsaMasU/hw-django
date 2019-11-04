import datetime

from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    RATE_CHOICES = [
        ('1', '★'),
        ('2', '★★'),
        ('3', '★★★'),
        ('4', '★★★★'),
        ('5', '★★★★★'),
    ]
    #public_date = forms.DateField(initial=datetime.date.today)
    text = forms.CharField(widget=forms.Textarea, label='Отзыв')
    stars = forms.CharField(label='Ваша оценка:', widget=forms.RadioSelect(choices=RATE_CHOICES))

    class Meta(object):
        model = Review
        # exclude = ('id', 'product')
        exclude = ()

    def clean(self):
        return self.cleaned_data
