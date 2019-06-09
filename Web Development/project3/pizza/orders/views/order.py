import json

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from ..models import MenuItem, Group, Order, MenuItemChoice, ExtraIngridient

from .general import index


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
        order = Order.objects.create(
            user=request.user,
            confirmation=False,
            address=request.POST["address"],
            phone=request.POST["telephone"],
        )
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
        return redirect(confirmation, id=order.id)
    return render(request, "orders/order.html", context)


# def check_order(func):
#     def wrapper(*args, **kwargs):
#         try:
#             order = Order.objects.get(id=kwargs["id"])
#         except:
#             print(kwargs)
#             print(args)
#             return redirect(menu)
#         if order.user == args[0].user:
#             return func(*args, **kwargs)
#         return redirect(menu)
#     wrapper.attrib = order
#     return wrapper
#
# @login_required
# @check_order
# def confirmation(request, id):
#     return render(request, "orders/confirmation.html", {"order": order})


@login_required
def confirmation(request, id):
    try:
        order = Order.objects.get(id=id)
    except:
        return redirect(menu)
    if order.user == request.user:
        return render(request, "orders/confirmation.html", {"order": order})
    return redirect(menu)


@login_required
def confirm(request, id):
    try:
        order = Order.objects.get(id=id)
    except:
        return redirect(menu)
    if order.user == request.user:
        order.confirmation = True
        order.save()
    return redirect(index)


@login_required
def orders(request):
    context = {"orders": Order.objects.filter(user=request.user)}
    return render(request, "orders/orders.html", context)
