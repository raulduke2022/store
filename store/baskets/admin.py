from django.contrib import admin

from .models import Basket, CartProduct

class AdminCartProduct(admin.ModelAdmin):
    list_display = ['product', 'basket', 'quantity']

class AdminBasket(admin.ModelAdmin):
    list_display = ['user']

admin.site.register(Basket, AdminBasket)
admin.site.register(CartProduct, AdminCartProduct)
