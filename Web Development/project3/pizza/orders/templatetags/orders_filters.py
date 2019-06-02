from django import template
from ..models import Group, MenuItem, MenuCombination
from django.contrib.auth.models import User

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


@register.filter
def get_current_user_name(session):
    u = User.objects.get(pk=session["_auth_user_id"])
    return u.first_name + " " + u.last_name
