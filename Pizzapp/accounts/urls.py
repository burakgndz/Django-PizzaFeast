from django.urls import path
from . import views

urlpatterns = [
    path('login', views.Login_view, name='login'),
    path('register', views.Register_view, name='register'),
    path('logout', views.Logout_view, name='logout'),
    path('card-info', views.CardInfo_view, name='card_info'),
    path('order-list', views.OrderList_view, name='order_list')


]
