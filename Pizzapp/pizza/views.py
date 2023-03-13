from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import messages

def Home(request):
    data = {
        'categories': Category.objects.all(),
        'pizza': Pizza.objects.filter(favorite=True)
    }
    return render(request, "pizza/index.html", data)

def PizzaPage(request,slug):
    data = {
        'categories': Category.objects.all(),
        'pizza': Pizza.objects.filter(category__name =slug),
        'selected_category': slug
    }
    return render(request, "pizza/pizza.html", data)

@login_required(login_url='login')
def OrderPizza(request):
    if not request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        if None in [request.user.tc_no, request.user.first_name,request.user.last_name,request.user.card_no,request.user.exp_month,request.user.exp_year,request.user.cv2,request.user.phone_number]:
            messages.warning(request,'Sipariş Verebilmeniz İçin Kart Bilgilerinizi Doldurmanız Gerekiyor!')
            return redirect("card_info")
        pizza = Pizza.objects.get(name=request.POST.get('pizza'))
        customer = request.user
        extras = request.POST.getlist('extra')
        size = request.POST['size']
        order = Order.objects.create(pizza=pizza,size=size, total_price=pizza.price, customer=customer)
        order.save()
        extra_price = 0
        for i in extras:
            extra_price += Extras.objects.get(id= int(i)).price    
            order.extra.add(int(i))
        if size == 'small':
            size_price = -20
        elif size == 'medium':
            size_price = 0
        else:
            size_price = 20
        order.total_price += extra_price + size_price
        order.save()

        return redirect('order')
    else:
        data = {

            'categories': Category.objects.all(),
            'pizza': Pizza.objects.all(),
            'extras': Extras.objects.all(),
            }
        return render(request, "pizza/orders.html", data )
    
