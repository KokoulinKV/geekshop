from django.db import models

from  users.models import User
from products.models import Product

# Create your models here.
class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    created_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Basket for {self.user.username} | Products {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price


    # def total_quantity(self):
    #     pass
    #
    # def total_price(self):
    #     pass