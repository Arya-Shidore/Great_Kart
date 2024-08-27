from django.shortcuts import render
from store.models import Product
from django.http import HttpResponse
# Create your views here.
def index(request):
    product = Product.objects.all().filter()
    context = {
        'product': product,
    }
    return render(request, 'index.html', context)