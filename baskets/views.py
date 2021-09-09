from django.shortcuts import HttpResponseRedirect
from products.models import Product
from baskets.models import Basket

# Create your views here.
def basket_add(request, id):
    product = Product.objects.get(id=id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        baskets = baskets.first()
        baskets.quantity += 1
        return  HttpResponseRedirect(request.META.get('HTTP_REFERER'))
