from django.shortcuts import render
import json

# Create your views here.


def index(request):
    data = 'products/templates/products/index.json'
    with open(data, 'r', encoding='utf-8') as products_json:
        context = json.load(products_json)
    return render(request, 'products/index.html', context)


def products(request):
    data = 'products/templates/products/products.json'
    with open(data, 'r', encoding='utf-8') as products_json:
        context = json.load(products_json)

    return render(request, 'products/products.html', context)
