from django import template
register = template.Library()

@register.filter
def cell_paint(value):
    color = 'blue'
    print(value)
    if(value == '---'):
        color = 'yellow'
        return color
    if((float(value)) > 1.0):
        color = 'red'
    print(color)
    return color