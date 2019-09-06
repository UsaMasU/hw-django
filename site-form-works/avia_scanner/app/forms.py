from django import forms

from .widgets import AjaxInputWidget
from .models import City

from django.forms.widgets import SelectDateWidget

MONTHS_CHOICES = {
    1:'Январь',
    2:'Февраль',
    3:'Март',
    4:'Апрель',
    5:'Май',
    6:'Июнь',
    7:'Июль',
    8:'Август',
    9:'Сентябрь',
    10:'Октябрь',
    11:'Ноябрь',
    12:'Декабрь'
}

class SearchTicket(forms.Form):
    departure = forms.CharField(label="Город отправления", widget=AjaxInputWidget(attrs={'class': 'inline right-margin'}, url='/api/city_ajax'))
    arrival = forms.ModelChoiceField(queryset=City.objects.all(), empty_label='----------------', label='Город назначения', widget=forms.Select())
    date_time = forms.DateField(label="Дата", widget=SelectDateWidget(months=MONTHS_CHOICES))
