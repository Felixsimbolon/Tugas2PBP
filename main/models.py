from django.db import models


class Product(models.Model):
    item = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
   