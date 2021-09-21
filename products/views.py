from django.shortcuts import render
import os
from products.models import Product, ProductCategory

MODULE_DIR = os.path.dirname(__file__)


# Create your views here.


def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context)


def products(request, id=None):
    if id != None:
        products_filter = Product.objects.filter(category_id=id)

    else:
        products_filter = Product.objects.all()
    context = {
        'title': 'GeekShop - Catalog',
        'categories': ProductCategory.objects.all()
    }
    context['products'] = products_filter
    return render(request, 'products/products.html', context)
