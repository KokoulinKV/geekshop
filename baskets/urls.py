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
# baskets_remove
from baskets.views import baskets_add, BasketRemove , baskets_edit

app_name = 'baskets'

urlpatterns = [
    path('baskets_add/<int:id>', baskets_add, name='baskets_add'),
    # path('baskets_remove/<int:id>', baskets_remove, name='baskets_remove'),
    path('baskets_remove/<int:pk>', BasketRemove.as_view(), name='baskets_remove'),
    path('baskets_edit/<int:id>/<int:quantity>/', baskets_edit, name='baskets_edit')
]
