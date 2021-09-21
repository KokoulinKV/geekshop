from django.contrib import admin

from baskets.models import Basket
# Register your models here.
admin.site.register(Basket)

#
# @admin.register(Basket)
# class BasketsAdmin(admin.ModelAdmin):
#     fields = ('name', 'product', 'quantity', 'created_timestamp', 'update_timestamp')
#     readonly_fields = ('created_timestamp', 'update_timestamp')