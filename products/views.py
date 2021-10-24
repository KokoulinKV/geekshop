from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os
from django.conf import settings

from django.views.generic import DetailView

from products.models import Product, ProductCategory

from django.core.cache import cache

MODULE_DIR = os.path.dirname(__file__)


# Create your views here.

def get_links_category():
    if settings.LOW_CACHE:
        key = 'links_category'
        links_category = cache.get(key)

        if links_category is None:
            links_category = ProductCategory.objects.filter(is_active=True)
            cache.set(key, links_category)
        return links_category
    else:
        return ProductCategory.objects.filter(is_active=True)

# def get_product(pk):
#     if settings.LOW_CACHE:
#         key = f'product{pk}'
#         product = cache.get(key)
#
#         if product is None:
#             product = get_object_or_404(Product,pk=pk)
#             cache.set(key, product)
#         return product
#     else:
#         return get_object_or_404(Product,pk=pk)


def get_links_product():
    if settings.LOW_CACHE:
        key = 'links_product'
        links_product = cache.get(key)

        if links_product is None:
            links_product = Product.objects.filter(is_active=True).select_related()
            cache.set(key, links_product)
        return links_product
    else:
        return Product.objects.filter(is_active=True).select_related()

def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context)


def products(request, id=None, page=1):
    if id != None:
        products_filter = Product.objects.filter(category_id=id).select_related('category')

    else:
        products_filter = Product.objects.all().select_related('category')
    products_filter = get_product()
    paginator = Paginator(products_filter, per_page=3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator(paginator.num_pages)
    context = {
        'title': 'GeekShop - Catalog',
        'categories': get_links_category()
    }
    context['products'] = products_paginator
    return render(request, 'products/products.html', context)


class ProductPage(DetailView):
    model = Product
    template_name = 'products/product_page.html'
    context_object_name = 'product'

    def get_context_data(self, category_id=None, *args, **kwargs):
        context = super().get_context_data()
        context['categories'] = ProductCategory.objects.all()
        return context