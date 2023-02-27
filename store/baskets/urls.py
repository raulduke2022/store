from django.urls import path

from .views import add_product

app_name = 'baskets'

urlpatterns = [
    path('add/<int:product_id>', add_product, name='basket'),
]