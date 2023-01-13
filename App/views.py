from email import message
from django.shortcuts import render, redirect
from .models import Post_New
from .models import Post_Discount
from .models import Post_Milk
from .models import Post_Soda
from .models import Post_Smoothies
from .models import Post_Recommended
from .models import Post_Cart
from .models import Post_List
from django.contrib.auth.models import User, auth
from django.contrib import messages

def index(request):
    data=Post_Recommended.objects.all()
    return render(request, 'index.html',{'posts':data})

def new(request):
    data=Post_New.objects.all()
    return render(request, 'new.html',{'posts':data})

def discount(request):
    data=Post_Discount.objects.all()
    return render(request, 'discount.html',{'posts':data})

def milk_tea(request):
    data=Post_Milk.objects.all()
    return render(request, 'milk_tea.html',{'posts':data})

def soda(request):
    data=Post_Soda.objects.all()
    return render(request, 'soda.html',{'posts':data})

def smoothies(request):
    data=Post_Smoothies.objects.all()
    return render(request, 'smoothies.html',{'posts':data})

def cart(request):
    total = 0
    cartItem = Post_Cart.objects.filter()
    count = Post_Cart.objects.all().count()
    for item in cartItem:
        total = total + item.price
    data=Post_Cart.objects.all()
    return render(request, 'cart.html',{'posts':data, 'total': total, 'count': count})
        
def add(request):
    total = 0
    if request.method == 'POST':
        name = request.POST.get('name', False)
        price = request.POST.get('price', False)
        image = request.POST.get('image', False)
        new = Post_Cart(name = name, price = price, image = image)
        new.save()
        data=Post_Cart.objects.all()
        cartItem = Post_Cart.objects.filter()
        for item in cartItem:
            total = total + item.price
        messages.success(request, "Add products to cart.")
    return render(request, 'cart.html',{'posts':data, 'total': total})

def delete(request, pk):
    new = Post_Cart.objects.get(id=pk)
    new.delete()
    messages.success(request, 'The product has been removed from the cart.')
    return redirect('/cart')

def search(request):
    textSearch = ''
    check = 0
    if 'textSearch' in request.GET:
        textSearch = request.GET['textSearch']
        if textSearch is '':
            data = ''
            check = 0
        else:
            data = Post_List.objects.filter(name__icontains=textSearch)
            count = Post_List.objects.filter(name__icontains=textSearch).count()
            if count == 0:
                check = 0
            else:
                check = 1
    else:
        data = ''
        check = 0
    return render(request, 'search.html',{'posts':data, 'check':check, 'textSearch':textSearch})

def register(request):
    return render(request, 'register.html')

def addUser(request):
    username = request.POST['username']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    repassword = request.POST['repassword']
    
    if password == repassword:
        if User.objects.filter(username=username).exists():
            messages.error(request, 'This username already exists.')
            return redirect('/register')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'This email already exists.')
            return redirect('/register')
        elif len(password)<8:
            messages.error(request, 'Password is too short.')
            return redirect('/register')
        else:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=firstname,
                last_name=lastname
            )   
            user.save()
            messages.success(request, 'Register complete.')
            return redirect('/login')
    else:
        messages.error(request, "Passwords don not match.")
        return redirect('/register')

def login(request):
    return render(request, 'login.html')

def userLogin(request):
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request,user)
        messages.success(request, 'Login complete.')
        return redirect('/user')
    else:
        messages.error(request, "User or Password is incorrect.")
        return redirect('/login')

def user(request):
    return render(request, 'user.html')

def logout(request):
    messages.success(request, "You are now logged out.")
    auth.logout(request)
    return redirect('/')

def payment(request):
    total = 0
    cartItem = Post_Cart.objects.filter()
    for item in cartItem:
        total = total + item.price
    return render(request, 'payment.html', {'total': total})

def buy(request):
    data = Post_Cart.objects.all()
    data.delete()
    messages.success(request, "Your payment was successful.")
    return redirect('/cart')

def about(request):
    return render(request, 'about.html')