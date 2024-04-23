from django import template

register = template.Library()

@register.filter(name='format_filename')
def format_filename(value):
    return value.replace(' ', '_') + '.webp'
