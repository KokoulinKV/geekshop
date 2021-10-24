"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from django.urls import path
from django.views.decorators.cache import cache_page

from products.views import products, ProductPage

app_name = 'products'

urlpatterns = [
    # path('', products, name='index'),
path('', cache_page(3600)(products), name='index'),
    path('category/<int:id>', products, name='category'),
    path('page/<int:page>', products, name='page'),
    path('product_page/<int:pk>', ProductPage.as_view(), name='product_page')

]
