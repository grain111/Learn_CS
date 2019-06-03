import json

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from ..models import MenuItem, Group, Order, MenuItemChoice, ExtraIngridient


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
        order_data = json.loads(request.POST["order"])
        order = Order.objects.create(user=request.user, confirmation=False)
        for item in order_data["items"]:
            choice = MenuItemChoice.objects.create(
                item=MenuItem.objects.get(
                    group=Group.objects.get(type=item["group"]), name=item["name"]
                ),
                order=order,
                size=item["size"],
            )
            for extra in item["extras"]:
                choice.extras.add(ExtraIngridient.objects.get(name=extra))
        return redirect(confirmation)
    return render(request, "orders/order.html", context)


@login_required
def confirmation(request):
    return render(request, "orders/index.html")
