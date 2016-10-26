from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Product, Genre, Artist, Admin, Order
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

###################################### USER ####################################################

def home(request):
    context = {'records' : Product.objects.all()}
    return render(request, "dope_vinyl/home.html", context)

def add_records(request):
    genre = Genre.objects.create(genre_type="Pop")
    artist = Artist.objects.create(name="Lady Gaga")
    Product.objects.create(genre=genre,image='imgs/Music/Pop/LadyGaga.jpg',artist=artist,title = "Joanne", price='29.99',inventory="100", description="dope record")
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

def front_allproducts_cat(request, id):
    products = Product.objects.filter(genre=id)
    paginator = Paginator(products,15)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    genres = Genre.objects.filter(id=id)
    context = {
        'products' : products,
        'genres' : genres,
    }
    return render(request, "dope_vinyl/front_allproducts.html", context)

def carts(request):




    return render(request, "dope_vinyl/front_shoppingcart.html")



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
           return redirect('/dashboard/orders')
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
