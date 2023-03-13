from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import MyUser
from pizza.models import Order, Category, Pizza, Extras



def Login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        username= request.POST['username']
        password= request.POST['password']
        user = authenticate(request, username= username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render( request, 'accounts/login.html', {
                'error': 'Kullanıcı adı veya parola geçersiz!!!'
            })    
    return render(request, 'accounts/login.html')


def Logout_view(request):
    logout(request)
    return redirect('home')


def Register_view(request):
    if request.user.is_authenticated:
        return redirect('home')    
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["repassword"]
        first_name = request.POST["firstname"]
        last_name = request.POST["lastname"]
        
        if password == password2:
            if len(password)<7:
                return render(request, "accounts/register.html",{
                    'error': 'parola en az 8 karakterden oluşmalı!',
                    })
            elif len(username)<4:
                return render(request, "accounts/register.html",{
                    'error': 'kullanıcı adı en az 5 karakterden oluşmalı!',
                    })               
        
            elif MyUser.objects.filter(username=username).exists():
                return render(request, "accounts/register.html",{
                        'error': 'Kullanıcı adı zaten var! Başka bir kullanıcı adı deneyiniz...',
                        'email':email,
                        'first_name': first_name,
                        'last_name': last_name
                     })
            else:
                if MyUser.objects.filter(email=email).exists():
                    return render(request, "accounts/register.html",{
                        'error': 'Bu email adresi zaten kayıtlı! Başka bir email adresi deneyiniz...',
                        'username':username,
                        'first_name': first_name,
                        'last_name': last_name                   
                        })
                else:
                    user = MyUser.objects.create_user(username=username, email= email, password=password, first_name=first_name,last_name=last_name)
                    user.save()
                    return redirect('login')
        else:
            return render(request, "accounts/register.html",{
                    'error': 'parola eşleşmiyor!',
                    'username':username,
                    'email':email,
                    'first_name': first_name,
                    'last_name': last_name
                    })
    return render(request, 'accounts/register.html')

@login_required(login_url='login')
def CardInfo_view(request):
    if request.method == "POST":
        phone_number = request.POST["phone_number"]
        tc_no = request.POST["tc_no"]
        card_no = request.POST["card_no"]
        cv2 = request.POST["cv2"]
        exp_month = request.POST["exp_month"]
        exp_year = request.POST["exp_year"]
        first_name = request.POST["firstname"]
        last_name = request.POST["lastname"]
        
        print("put:", request.POST)
        print("-----------")
        print(phone_number)
        print(type(phone_number))


        if len(str(phone_number)) != 10:
            data = {
                "error": '10 haneli geçerli bir telefon numarası giriniz!',
            }
            return render(request, "accounts/card_info.html", data)
        elif len(str(tc_no)) != 11:
            data = {
                "error": '11 haneli geçerli bir TC kimlik numarası giriniz!',
            }
            return render(request, "accounts/card_info.html", data)
                    
        elif len(str(card_no)) != 16:
            data = {
                "error": '16 haneli geçerli bir kart numarası giriniz!',
            }
            return render(request, "accounts/card_info.html", data)
        
        elif int(exp_month) < 0 or int(exp_month)>12 :
            data = {
                "error": 'Geçerli bir ay giriniz!',
            }
            return render(request, "accounts/card_info.html", data)
        
        elif int(exp_year) < 2023 or int(exp_year) > 2030 :
            data = {
                "error": 'Geçerli bir yıl giriniz!',
            }
            return render(request, "accounts/card_info.html", data) 
        else:
            user = MyUser.objects.get(id=request.user.id)
            user.first_name = first_name
            user.last_name = last_name
            user.phone_number = phone_number
            user.exp_month = exp_month
            user.exp_year = exp_year
            user.tc_no = tc_no
            user.card_no = card_no
            user.cv2 = cv2
            user.save()
            
            return redirect("order")
  
    data = {
        "info": MyUser.objects.get(id= request.user.id),
        
    }
    return render(request, "accounts/card_info.html", data)



@login_required(login_url='login')
def OrderList_view(request):
    order = Order.objects.filter(customer=request.user.id)
    user_orders_id = [i.id for i in order]
    extras_names = {}
    for id in user_orders_id:
        extras_names[id]= [i.name for i in Extras.objects.filter(order= id)]
    
    data = {
        "categories": Category.objects.all(),
        "extras": extras_names,
        "zipped": zip(order,list(range(1,len(order)+1)))
    }
    return render(request, "accounts/order_list.html", data)

