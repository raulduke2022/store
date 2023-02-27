# Generated by Django 4.1.6 on 2023-02-25 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('baskets', '0002_basketproductquantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='basketproductquantity',
            name='basket_products',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='products.product'),
        ),
    ]