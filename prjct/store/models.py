import uuid
from django.db import models
from django.db.models.deletion import CASCADE


class Product(models.Model):
    product_image = models.FileField(
        upload_to='static/images/products', blank=True)
    product_title = models.CharField(max_length=50)
    product_price = models.FloatField()

    def __str__(self):
        return self.product_title


class Cart(models.Model):
    product = models.ManyToManyField(Product)
