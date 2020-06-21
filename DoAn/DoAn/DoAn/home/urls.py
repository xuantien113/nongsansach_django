from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home, name="home"),
    path('index', views.Index, name="index"),
    # path('shop', views.Shop, name="shop"),
    # path('shop/<int:detail_id>', views.Shop, name="shop_product"),
    path('login', views.Login, name="login"),
    path('checkout',views.Checkout,name="checkout"),
    path('contact',views.Contact, name="contact"),
    path('blog',views.Blog, name="blog"),
    path('about',views.About, name="about"),
    path('blog-single',views.Blogsingle, name="blogsingle"),
    path('wishlist',views.Wishlist, name="wishlist"),
    path('product-single/<int:product_id>',views.Productsingle, name='product'),
    path('cart',views.Cart, name="cart"),
    path('register',views.Register, name="register")
]
