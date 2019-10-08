from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("menu", views.menu, name="menu"),
    path("about", views.about, name="about"),
    path("register", views.register, name="register"),
    path("cart", views.cart, name="cart"),
    path("addons", views.addons, name="addons")
]
