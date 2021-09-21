from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os

from products.models import Product, ProductCategory

MODULE_DIR = os.path.dirname(__file__)


# Create your views here.


def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context)


def products(request, id=None, page=1):
    if id != None:
        products_filter = Product.objects.filter(category_id=id)

    else:
        products_filter = Product.objects.all()
    paginator = Paginator(products_filter, per_page=3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator(paginator.num_pages)
    context = {
        'title': 'GeekShop - Catalog',
        'categories': ProductCategory.objects.all()
    }
    context['products'] = products_paginator
    return render(request, 'products/products.html', context)
