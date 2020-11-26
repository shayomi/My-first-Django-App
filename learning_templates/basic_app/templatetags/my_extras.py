from django import template

register = template.Library()
@register.filter('cut')

def cut(value, arg):
    """
    this cuts out the value of "arg" from the string
    """
    return value.replace(arg, '')

# register.filter('cut', cut)
