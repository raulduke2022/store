from django.db import models
from users.models import User
from products.models import Product


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    created = models.DateTimeField(auto_now_add=True)

    # def count_products(self):
    #     return self.products.all().count()



