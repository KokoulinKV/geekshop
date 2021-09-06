from django.shortcuts import render
import json
import os
from products.models import  Product, ProductCategory


MODULE_DIR = os.path.dirname(__file__)
# Create your views here.


def index(request):
    context = {'title':'GeekShop'}
    return render(request, 'products/index.html', context)

def products(request):
    context = {'title':'GeekShop - Catalog'}
    context['categories'] = ProductCategory.objects.all()
    context['products'] = Product.objects.all()
    return render(request, 'products/products.html', context)
#
# def products(request):
#     data = os.path.join(MODULE_DIR, 'fixtures/products.json')
#     with open(data, 'r', encoding='utf-8') as products_json:
#         context = json.load(products_json)
#
#     return render(request, 'products/products.html', context)
