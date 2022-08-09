from django import template

register = template.Library()

def cut(value, arg):
    return value.replace(arg,'')

register.filter('cut',cut)

@register.filter #(name='lower')
def lower(value):
    return value.lower()
