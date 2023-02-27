from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=144)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/images')
    category = models.ForeignKey(to='ProductCategory', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
