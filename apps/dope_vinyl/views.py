from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Product, Genre, Artist, Admin, Order
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

###################################### USER ####################################################

def home(request):
    context = {'records' : Product.objects.all()}
    return render(request, "dope_vinyl/home.html", context)

def add_records(request):
    genre = Genre.objects.filter(genre_type="Pop")[0]
    artist = Artist.objects.create(name="Taylor Swift")
    Product.objects.create(genre=genre,image='imgs/Music/Pop/TaylorSwift.jpg',artist=artist,title = "T.S. 1989", price='19.99',inventory="100", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras ullamcorper, arcu sed interdum ullamcorper, purus diam scelerisque arcu, eget tristique ligula odio sed orci. Pellentesque quis eros in tellus dignissim rutrum. Suspendisse mattis venenatis velit. Nulla faucibus sagittis rhoncus. Praesent consequat et nisl sed facilisis. Vestibulum eget diam massa. Praesent arcu augue, pretium vel libero nec, congue bibendum tortor. Ut id condimentum dui. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Etiam rutrum, ipsum ac interdum ultrices, elit elit suscipit sem, sed mattis augue velit sit amet neque. Aenean id velit enim. Sed fringilla accumsan orci eget sagittis. In nisl mi, dictum sit amet massa vitae, auctor ullamcorper ligula.")
    return redirect('/')



def front_allproducts(request):
    try:
        sort=request.POST['sort']
    except:
        sort='title'
    products = Product.objects.all().order_by(sort)
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
        'sort_current' : sort,
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

def front_productpage(request, id):
    product = Product.objects.get(id=id)
    similar_products = Product.objects.filter(genre=product.genre)
    context = {
        'product': product,
        'similar_products': similar_products
        }
    return render(request, "dope_vinyl/front_productpage.html", context)

def buy(request, id):

    return redirect('/front_allproducts')

def carts(request):




    return render(request, "dope_vinyl/front_shoppingcart.html")

def billing_shipping(request):
    stripe.api_key = "sk_test_MtYKfrdjHXRPAAuSul1W5m5B"
    token = request.POST['stripeToken']
    try:
      charge = stripe.Charge.create(
          amount=1000,
          currency="usd",
          source=token,
          description="Example charge"
      )
    except stripe.error.CardError as e:
      # The card has been declined
      pass


    return redirect('/dashboard/orders')



###################################### ADMIN ###################################################
def admin(request):
    return render(request, "dope_vinyl/adminlogin.html")


def adminlogin(request):
   if request.method == "POST":
       admin = Admin.objects.login(request.POST)
       #then goes to models login
       if not admin:
           messages.error(request, "Invalid login credentials!")
       else:
           request.session['logged_admin'] = admin.id
           return redirect('/dashboard/orders')
   return redirect('/admin')

### we put one admin into the DB's Admin table.
###     The login is: dope.vinyl.admin@gmail.com (all lowercase)
###     The password is: dope (all lowercase)
def adminlogout(request):
    if 'logged_admin' in request.session:
        request.session.pop('logged_admin')
    return redirect('/admin')

############################################### DASHBOARD #######################################
#ALL ORDERS ON ADMIN PAGE.
def orders(request):
<<<<<<< HEAD

    return render(request, 'dope_vinyl/dashboard_allorders.html')
=======
    if 'logged_admin' not in request.session:
        messages.error(request, "Gotta login bro")
        return redirect('/adminlogin')
    context = {
        'admin': Admin.objects.get(id=request.session['logged_admin'])
    }

    return render(request, 'dope_vinyl/dashboard_allorders.html', context)
>>>>>>> 907a69e3168bf4f6f24c767c827e5c01ca53d63f


#INDIVIDUAL ORDER ON ADMIN PAGE.
def show_orders(request):

    return render(request, 'dope_vinyl/dashboard_showorder.html')

#ALL PRODUCTS ON ADMIN PAGE. CLICK ON ADD NEW PRODUCT TO TAKE YOU TO ADD/EDIT ROUTE.

def products(request):
    if 'logged_admin' not in request.session:
        messages.error(request, "Gotta login bro")
        return redirect('/adminlogin')
    all_products = Product.objects.all()
    all_genres = Genre.objects.filter()

    context = {
        "all_products": all_products,
        "all_genres": all_genres
    }
    return render(request, 'dope_vinyl/dashboard_allproducts.html', context)

def products_add(request):
    if request.method == "POST":
        if request.POST['genre_new'] != "":
            artist_name = Artist.objects.create(name=request.POST['artist'])
            genre_type = Genre.objects.create(genre_type=request.POST['genre_new'])
            Product.objects.create(artist=artist_name, title=request.POST['title'],description=request.POST['description'],genre=genre_type, price=request.POST['price'], inventory=request.POST['inventory'], image=request.FILES['image'])

        elif request.POST['genre'] != "":
            artist_name = Artist.objects.create(name=request.POST['artist'])
            genre_type = Genre.objects.get(genre_type=request.POST['genre'])
            Product.objects.create(artist=artist_name, title=request.POST['title'],description=request.POST['description'],genre=genre_type, price=request.POST['price'], inventory=request.POST['inventory'], image=request.FILES['image'])

    return redirect("/dashboard/products")

def products_edit(request):

    if request.method == "POST":
        if request.POST['genre_new'] != "":
            genre_type = request.POST['genre_new']
            Product.objects.get(id=request.POST['id']).update(artist=artist_name, title=request.POST['title'],description=request.POST['description'],genre=genre_type, price=request.POST['price'], inventory=request.POST['inventory'], image=request.FILES['image'])

        elif request.POST['genre'] != "":
            genre_type = request.POST['genre']
            Product.objects.get(id=request.POST['id']).update(artist=artist_name, title=request.POST['title'],description=request.POST['description'],genre=genre_type, price=request.POST['price'], inventory=request.POST['inventory'], image=request.FILES['image'])

    return redirect("/dashboard/products")


def products_delete(request, id):
    Product.objects.get(id=id).delete()
    return redirect("/dashboard/products")
