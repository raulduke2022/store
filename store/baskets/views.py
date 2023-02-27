from django.shortcuts import HttpResponseRedirect
from .models import Basket


def add_product(request, product_id):
    basket = Basket.objects.filter(user=request.user)
    if basket:
        basket[0].products.add(product_id)
    else:
        basket = Basket.objects.create(user=request.user)
        basket.products.add(product_id)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
