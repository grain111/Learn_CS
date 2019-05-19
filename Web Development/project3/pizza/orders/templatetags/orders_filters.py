from django import template
from ..models import Group, MenuItem, MenuCombination

register = template.Library()


@register.filter
def span(i):
    return range(i)

@register.filter
def get_items_by_group(group):
    return MenuItem.objects.filter(group=Group.objects.get(type=group))

@register.filter
def get_menu_combination_price(item, extra):
    return MenuCombination.objects.get(extra=extra, item=item).price
