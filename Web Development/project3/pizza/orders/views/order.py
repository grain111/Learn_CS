import json

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from ..models import MenuItem, Group


@login_required
def menu(request):
    context = {
        "groups": Group.objects.all(),
        "items": {
            group.type: MenuItem.objects.filter(group=group)
            for group in Group.objects.all()
        },
    }
    return render(request, "orders/menu.html", context)


@login_required
def order(request):
    context = {}
    if request.method == "POST":
        order = json.loads(request.POST["order"])
        for item in order["items"]:
            print(item)
    return render(request, "orders/order.html", context)
