from django.shortcuts import render
import json
import os


MODULE_DIR = os.path.dirname(__file__)
# Create your views here.


def index(request):
    data = os.path.join(MODULE_DIR, 'fixtures/index.json')
    with open(data, 'r', encoding='utf-8') as products_json:
        context = json.load(products_json)
    return render(request, 'products/index.html', context)


def products(request):
    data = os.path.join(MODULE_DIR, 'fixtures/products.json')
    with open(data, 'r', encoding='utf-8') as products_json:
        context = json.load(products_json)

    return render(request, 'products/products.html', context)
