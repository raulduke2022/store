from django.contrib import admin

from .models import Basket, BasketProductQuantity


admin.site.register(Basket)
admin.site.register(BasketProductQuantity)