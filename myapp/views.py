from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Category, Product

# Create your views here.

def index(request):
    return render(request,'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if not remember_me:
                request.session.set_expiry(0)  # Session expires when browser closes
            messages.success(request, 'Login successful!')
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')


# ===========================================
# UPDATED FUNCTION (LOAD PRODUCTS HERE)
# ===========================================
def shop_grid(request):
    products = Product.objects.all()  
    return render(request, 'shop-grid.html', {'products': products})


def shop_details(request):
    pro = Product.objects.all()
    return render(request, 'shop-details.html', {'pros': pro})


def shoping_cart(request):
    return render(request, 'shoping-cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def blog(request):
    return render(request, 'blog.html')

def blog_details(request):
    return render(request, 'blog-details.html')

def contact(request):
    return render(request, 'contact.html')


def register(request):
    if request.method == 'POST':
        # Use the form field names from the template (`register.html`)
        fn = request.POST.get('fname')
        ln = request.POST.get('lname')
        un = request.POST.get('uname')
        em = request.POST.get('email')
        p1 = request.POST.get('pass1')
        p2 = request.POST.get('pass2')

        # Validate and show errors on the same page instead of redirecting
        if p1 != p2:
            messages.error(request, 'Passwords do not match!')
            return render(request, 'register.html')

        if not un:
            messages.error(request, 'Username is required!')
            return render(request, 'register.html')

        if User.objects.filter(username=un).exists():
            messages.error(request, 'Username already exists!')
            return render(request, 'register.html')

        if em and User.objects.filter(email=em).exists():
            messages.error(request, 'Email already exists!')
            return render(request, 'register.html')

        User.objects.create_user(
            first_name=fn,
            last_name=ln,
            username=un,
            email=em,
            password=p1
        )
        messages.success(request, 'Account created successfully! Please log in.')
        return redirect('login')
    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    print('Logout successfully!')
    return redirect('index')
def product_details(request, pid):
    product = Product.objects.get(pid=pid)
    return render(request, 'product-details.html', {'product': product})
