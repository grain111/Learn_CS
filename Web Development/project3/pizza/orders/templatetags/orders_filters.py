from django import template

register = template.Library()


@register.filter
def span(i):
    return range(i)
