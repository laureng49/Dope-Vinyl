from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Product, Genre, Artist, Admin, Order
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

###################################### USER ####################################################

def home(request):
    context = {'records' : Product.objects.all()}
    return render(request, "dope_vinyl/home.html", context)

def add_records(request):
    genre = Genre.objects.create(genre_type="Country")
    artist = Artist.objects.create(name="Johnny Cash")
    Product.objects.create(genre=genre,image='imgs/Music/Country/JohnnyCash.jpg',artist=artist,title = "At Folsom Prison", price='29.99',inventory="100")
    return redirect('/')

def front_allproducts(request):
    products = Product.objects.all()
    paginator = Paginator(products,15)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    genres = Genre.objects.all()
    context = {
        'products' : products,
        'genres' : genres,
    }
    return render(request, "dope_vinyl/front_allproducts.html", context)

def front_allproducts_cat(id):
    products = Product.objects.filter(genre=id)
    paginator = Paginator(products,15)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    genres = Genre.objects.get(id=id)
    context = {
        'products' : products,
        'genres' : genres,
    }
    return redirect('/front_allproducts')

###################################### ADMIN ###################################################
def admin(request):
    return render(request, "dope_vinyl/adminlogin.html")


def adminlogin(request):
   #either they're good at logging in or not
   if request.method == "POST":
       admin = Admin.objects.login(request.POST)
       # print admin.values()
       # logged_admin = Admin.objects.get(id=request.session['logged_admin'])

       if not admin:
           messages.error(request, "Invalid login credentials!")

       else:
           # request.session['admin'] = admin.id
           return redirect('/dashboard_allorders')
   return redirect('/admin')

### we put one admin into the DB's Admin table.
###     The login is: dope.vinyl.admin@gmail.com (all lowercase)
###     The password is: dope (all lowercase)

############################################### DASHBOARD #######################################
#ALL ORDERS ON ADMIN PAGE.
def orders(request):
    return render(request, 'dope_vinyl/dashboard_allorders.html')

#ALL PRODUCTS ON ADMIN PAGE. CLICK ON ADD NEW PRODUCT TO TAKE YOU TO ADD/EDIT ROUTE.
def products(request):
    products = Product.objects.all()
    print products.values()
    context = {
        "products": products
    }
    return render(request, 'dope_vinyl/dashboard_allproducts.html', context)

def products_add(request):
    return redirect("/dashboard/products/insert")
