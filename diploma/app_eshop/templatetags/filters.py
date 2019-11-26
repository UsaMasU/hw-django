from django import template

register = template.Library()


@register.filter
def get_items(value, arg=''):
    result = ''
    if isinstance(value, dict):
        result = value.get(arg, '')
    return result
