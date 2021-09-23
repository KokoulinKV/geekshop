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

from admins.views import index,  admins_users_update, admins_users_create, admins_users_delete, \
    admins_products, admins_products_create, admins_products_update, admins_products_delete, admins_users_rehub, UserListView
# admins_users
app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admins_users'),
    # path('users/', admins_users, name='admins_users'),
    path('users-update/<int:id>', admins_users_update, name='admins_users_update'),
    path('users-create/', admins_users_create, name='admins_users_create'),
    path('users-delete/<int:id>', admins_users_delete, name='admins_users_delete'),
    path('products/', admins_products, name='admins_products'),
    path('products-create/', admins_products_create, name='admins_products_create'),
    path('products-update/<int:id>', admins_products_update, name='admins_products_update'),
    path('products-delete/<int:id>', admins_products_delete, name='admins_products_delete'),
    path('users_rehub/<int:id>', admins_users_rehub, name='admins_users_rehub'),

]
