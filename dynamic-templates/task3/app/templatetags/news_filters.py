from django import template
import datetime
import time
register = template.Library()



@register.filter
def format_date(value):
    # Ваш код
    #print(value)
    dt = datetime.datetime.fromtimestamp(value).timetuple()
    print('post time:', dt)
    return value


# необходимо добавить фильтр для поля `score`


@register.filter
def format_num_comments(value):
    # Ваш код
    return value



