from django import template

register = template.Library()

@register.filter(name='rep')
def rep(value,arg):
    """
    Deletes the word from the string
    """
    return value.replace(arg,'')