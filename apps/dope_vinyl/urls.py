from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.home),
    url(r'^add_records$', views.add_records),
    url(r'^show$', views.home),
    # url(r'^dashboard/products$', views.products),
    url(r'^front_allproducts$', views.front_allproducts),
    url(r'^front_allproducts/page(?P<page>[0-9]+)/$', views.front_allproducts),
    url(r'^front_allproducts/category/(?P<id>\d+)$', views.front_allproducts_cat),
    # url(r'^sort_products/(?P<id>\w+)$', views.sort_products),
    url(r'^front_productpage/show/(?P<id>\d+)$', views.front_productpage),
    url(r'^front_productpage/buy/(?P<id>\d+)$', views.buy),
    url(r'^admin$', views.admin),
    url(r'^adminlogin$', views.adminlogin),
    url(r'^adminlogout$', views.adminlogout),
    url(r'^dashboard/products$', views.products), #TEMPLATE
    url(r'^dashboard/products/add$', views.products_add),
    # url(r'^dashboard/products/edit/(?P<id>\d+)$', views.products_edit),
    url(r'^dashboard/orders$', views.orders),
    # url(r'^adminlogout$', views.adminlogout),
    url(r'^carts$', views.carts),


#     url(r'^home$', views.home),
#     url(r'^carts$', views.carts),
#     url(r'^admin$', views.admin),
#     url(r'^category$', views.category),
#     url(r'^category/(?P<category_id>\d+)$', views.category_page),
#     url(r'^dashboard/products$', views.products),
#     url(r'^products/show/(?P<product_id>\d+)$', views.product_page),
#     url(r'^dashboard/orders$', views.orders),
]
