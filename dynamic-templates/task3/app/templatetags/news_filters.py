from django import template
import datetime

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

@register.filter
def format_score(value = 0):
    if (value > 5):
        score_message = 'хорошо'
        return f'{score_message}'
    if(value < -5):
        score_message = 'все плохо'
        return f'{score_message}'
    if (value > -5 and value < 5):
        score_message = 'нейтрально'
        return f'{score_message}'

@register.filter
def format_num_comments(value):
    if (value > 50):
        comments_message = '50+'
        return f'{comments_message}'

    if (value > 0 and value < 50):
        comments_message = str(value)
        return f'{comments_message}'

    if(value == 0):
        comments_message = 'Оставьте комментарий'
        return f'{comments_message}'

@register.filter
def format_selftext(text, count):
    str_start = ''
    for word in text.split(' ')[0:count]:
        str_start += word + ' '

    str_end = ' '
    for word in text.split(' ')[-count:]:
        str_end += word + ' '

    return f'{str_start}...{str_end}'



