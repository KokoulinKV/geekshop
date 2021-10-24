from django.db import models
from django.utils.functional import cached_property

from users.models import User
from products.models import Product


class BasketQuerySet(models.QuerySet):

    def delete(self, *args, **kwargs):
        for item in self:
            item.product.quantity -= item.quantity
            item.product.save()
        super(BasketQuerySet, self).delete(*args, **kwargs)


class Basket(models.Model):
    objects = BasketQuerySet.as_manager()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    created_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Basket for {self.user.username} | Products {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price

    @cached_property
    def get_items_cached(self):
        return self.user.basket.select_related()

    def total_quantity(self):
        items = self.get_items_cached
        return sum(item.quantity for item in items)

    def total_price(self):
        items = self.get_items_cached
        return sum(item.sum() for item in items)

    @staticmethod
    def get_item(pk):
        return Basket.objects.get(pk=pk).quantity

    def delete(self,*args,**kwargs):
        self.product.quantity += self.quantity
        self.save()
        super(Basket, self).delete(*args, **kwargs)


    def save(self, *args, **kwargs):
        super(Basket, self).save(*args, **kwargs)