from django.contrib import admin

from .models import Product, ProductCategory

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price']



admin.site.register(ProductCategory)
admin.site.register(Product, AdminProduct)
