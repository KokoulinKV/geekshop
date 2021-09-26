from django.contrib import admin

from baskets.models import Basket
from users.models import User
from baskets.admin import BasketsAdmin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = Basket
    inlines = (BasketsAdmin,)
