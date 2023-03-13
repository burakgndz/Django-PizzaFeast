from django.urls import path
from . import views
urlpatterns = [
    path("", views.Home, name='home'),
    path("<slug:slug>", views.PizzaPage, name= 'pizza'),
    path("create-order/", views.OrderPizza, name="order"),
]