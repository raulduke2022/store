from django.shortcuts import HttpResponseRedirect
from .models import Basket, CartProduct
from products.models import Product


def add_product(request, product_id):
    basket = Basket.objects.filter(user=request.user)
    if basket:
        if basket[0].products.filter(id=product_id):
            basket[0].cartproduct_set.filter(product__id=product_id)[0].quantity = 10
            basket[0].cartproduct_set.filter(product__id=product_id)[0].save()
        else:
            basket[0].products.add(product_id)
            CartProduct.objects.create(product=Product.objects.get(pk=product_id), basket=basket[0], quantity=1)
    else:
        Basket.objects.create(user=request.user)
        add_product(request, product_id)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
