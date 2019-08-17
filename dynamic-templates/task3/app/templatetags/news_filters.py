from django import template
import datetime
import time
register = template.Library()



@register.filter
def format_date(value):
    dt_now = datetime.datetime.now()
    dt_sp_minutes = dt_now - datetime.timedelta(minutes = 10)
    dt_sp_hours = dt_now - datetime.timedelta(hours = 24)
    dt_post = datetime.datetime.fromtimestamp(value)
    dt_dif = dt_now - dt_post

    if(dt_post >= dt_sp_minutes):
        dt_message = 'только что'
        return f'{dt_message}'

    if (dt_post >= dt_sp_hours):
        dt_message = str(dt_dif.seconds / 60 / 60).split('.')[0]
        return f'{dt_message} часов назат'

    if (dt_post < dt_sp_hours):
        dt_message = str(dt_post.date())
        return f'{dt_message}'

# необходимо добавить фильтр для поля `score`
@register.filter
def format_score(value):

    return value

@register.filter
def format_num_comments(value):
    # Ваш код
    return value



