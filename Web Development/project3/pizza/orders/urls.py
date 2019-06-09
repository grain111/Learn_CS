from django.urls import path

from . import views

urlpatterns = [
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("", views.index, name="index"),
    path("logout", views.logout_view, name="logout"),
    path("menu", views.menu, name="menu"),
    path("order", views.order, name="order"),
    path("confirmation/<int:id>", views.confirmation, name="confirmation"),
    path("orders", views.orders, name="orders"),
    path("confirm/<int:id>", views.confirm, name="confirm"),
]
