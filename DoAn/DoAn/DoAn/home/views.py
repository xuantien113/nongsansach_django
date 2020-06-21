from django.shortcuts import render, redirect
from home.models import Product, Product_detail
from django.contrib.auth.models import User,auth
from home.forms import SearchForm
from home.filters import ProductFilter
# Create your views here.
from django.http import Http404, HttpResponse, HttpResponseRedirect


def home(request):

    # sanpham = SanPham.objects.all()
    # extra_context = {"sanpham": sanpham}

    # return render(request, 'index.html', extra_context)
    product = Product.objects.all()
    product_detail = Product_detail.objects.all()
    product_laster = Product_detail.objects.all().order_by('-id')[:4]
    extra_context = {
        'product': product,
        'product_detail': product_detail,
        'product_laster': product_laster
    }
    return render(request, 'index.html', extra_context)

def Index(request):
    product = Product.objects.all()
    product_laster = Product_detail.objects.all().order_by('-id')[:4]
    extra_context ={
        'product': product,
        'product_laster':product_laster
    }
    return render(request, 'index.html', extra_context)

def search(request):
    query = Product.objects.all()
    product_filter =ProductFilter(request.GET, queryset=query)
    
    extra_context = {
        'form': product_filter.form,
        'product': product_filter.qs
    }
    return render(request, 'shop.html',extra_context)

def Shop(request):
    product = Product.objects.all()
    product_laster = Product_detail.objects.all().order_by('-id')[:4]
    extra_context ={
        'product': product,
        'product_laster':product_laster
    }
    return render(request, 'shop.html', extra_context)


def shop_product(request, detail_id):
    product = Product.objects.filter(product_detail_id = detail_id )
    product_laster = Product_detail.objects.all().order_by('-id')[:4]
    extra_context ={
        'product': product,
        'product_laster':product_laster
    }
    return render(request, 'shop.html', extra_context)

def Login(request):
        product = Product.objects.all()
        product_laster = Product_detail.objects.all().order_by('-id')[:4]
        extra_context ={
            'product': product,
            'product_laster':product_laster
        }
        return render(request, 'login.html', extra_context)

def Checkout(request):
    product = Product.objects.all()
    product_laster = Product_detail.objects.all().order_by('-id')[:4]
    extra_context ={
        'product': product,
        'product_laster':product_laster
    }
    return render(request, 'checkout.html', extra_context)


def Contact(request):
    product = Product.objects.all()
    product_laster = Product_detail.objects.all().order_by('-id')[:4]
    extra_context ={
        'product': product,
        'product_laster':product_laster
    }
    return render(request, 'contact.html', extra_context)

def Blog(request):
    product = Product.objects.all()
    product_laster = Product_detail.objects.all().order_by('-id')[:4]
    extra_context ={
        'product': product,
        'product_laster':product_laster
    }
    return render(request, 'blog.html', extra_context)

def Blogsingle(request):
    product = Product.objects.all()
    product_laster = Product_detail.objects.all().order_by('-id')[:4]
    extra_context ={
        'product': product,
        'product_laster':product_laster
    }
    return render(request, 'blog-single.html', extra_context)

def Cart(request):
    # if request.user.is_authenticated:
    #     customer = request.user.customer
    #     order, created = Order.objects.get_or_create(customer=customer, complete=False)
    #     atems = order.orderitem_set.all()
    # else:
    #         atems = []
    #         extra_context = {
    #             "atems": atems
    #             }
    # # return render(request, 'cart.html',{'extra_context':extra_context})
    # return render(request,'cart.html', extra_context)

    return render(request, 'cart.html')
    
def Wishlist(request):
    product = Product.objects.all()
    product_laster = Product_detail.objects.all().order_by('-id')[:4]
    extra_context ={
        'product': product,
        'product_laster':product_laster
    }
    return render(request, 'wishlist.html', extra_context)

def About(request):
    product = Product.objects.all()
    product_laster = Product_detail.objects.all().order_by('-id')[:4]
    extra_context ={
        'product': product,
        'product_laster':product_laster
    }
    return render(request, 'about.html', extra_context)

def Productsingle(request, product_id):
    # sanpham = SanPham.objects.get(id = sanpham_id)
    # return render(request, 'product-single.html', {"sanpham": sanpham})
    product = Product.objects.get(id = product_id)
    product_laster = Product_detail.objects.all().order_by('-id')[:4]
    extra_context ={
        'product': product,
        'product_laster':product_laster
    }
    return render(request, 'product-single.html',extra_context)

def Register(request):
    product = Product.objects.all()
    product_laster = Product_detail.objects.all().order_by('-id')[:4]
    extra_context ={
        'product': product,
        'product_laster':product_laster
    }
    return render(request, 'register.html',extra_context)
