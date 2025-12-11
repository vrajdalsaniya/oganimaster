from django.urls import path
from .views import *

urlpatterns = [

    path('', index, name='index'),
    path('index.html/', index, name='index_html'),
    path('login/', login_view, name='login'),
    path('shop-grid/', shop_grid, name='shop_grid'),
    path('shop-details/', shop_details, name='shop_details'),
    path('shoping-cart/', shoping_cart, name='shoping_cart'),
    path('checkout/', checkout, name='checkout'),
    path('blog/', blog, name='blog'),
    path('blog-details/', blog_details, name='blog_details'),
    path('contact/', contact, name='contact'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('product/<int:pid>/', product_details, name='product_details'),

]
