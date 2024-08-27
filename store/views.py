from django.shortcuts import render
from .models import Product
from category.models import Category
from cart.views import _cart_id
from cart.models import CartItem
# Create your views here.
def store(request):
    product=Product.objects.all().filter(is_available=True)
    context={
        'product':product,
    }
    return render(request, 'store/store.html',context)


def category(request,category_slug):
    product=None
    category=None
    if category_slug!=None:
        category=Category.objects.get(slug=category_slug)
        product=Product.objects.all().filter(category=category,is_available=True)
        product_count=product.count()
    else:
        product=Product.objects.all().filter(is_available=True)
        product_count=product.count()
    context={
        'product':product,
        'product_count':product_count,
    }
    return render(request, 'store/store.html',context)


def product_detail(request,category_slug,product_slug):
    try:
        single_product=Product.objects.get(category__slug=category_slug,slug=product_slug)
        in_cart=CartItem.objects.filter(cart__cart_id=_cart_id(request),product=single_product).exists()
    except Exception as e:
        raise e
    context={
        'single_product':single_product,
        'in_cart':in_cart,
    }
    return render(request, 'store/product_detail.html',context)
