from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.

def index(request):
    return render(request, 'farm/index.html')


def product(request):
    products= Product.objects.all()
    context = {
        'product':products,
    }
    return render(request, 'farm/products.html', context)
