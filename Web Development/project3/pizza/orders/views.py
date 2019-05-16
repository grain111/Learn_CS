from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Group, ExtraIngridient, MenuItem


@login_required
def index(request):
    return render(request, "orders/index.html")


def register(request):
    context = {}
    if request.method == "POST":
        username = request.POST["user_name"]
        email = request.POST["email"]

        if (
            not User.objects.filter(username=username).exists()
            and not User.objects.filter(email=email).exists()
        ):
            user = User.objects.create_user(
                username=request.POST["user_name"],
                password=request.POST["password"],
                email=request.POST["email"],
                first_name=request.POST["first_name"],
                last_name=request.POST["last_name"],
            )
            user.save()
            return redirect(login_view)
        context["msg"] = "Username or email already in database."
    return render(request, "orders/registration/register.html", context)


def logout_view(request):
    logout(request)
    return redirect(index)


def login_view(request):
    context = {}
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST["user_name"],
            password=request.POST["password"],
        )
        if user is not None:
            login(request, user)
            return redirect(index)
        else:
            context["msg"] = "Username or password incorrect."
    return render(request, "orders/registration/login.html", context)


@login_required
def menu(request):
    context = {
        "groups": Group.objects.all(),
        "items": {
            group.type: MenuItem.objects.filter(group=group)
            for group in Group.objects.all()
        },
    }
    print(context["items"])
    return render(request, "orders/menu.html", context)
