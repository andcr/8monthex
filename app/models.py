from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=30, null=False, blank=True)
    price = models.IntegerField(max_length=40, null=False, blank=True)
    date = models.DateField(null=False, blank=True)


class Customers(models.Model):
    name = models.CharField(max_length=30, null=False, blank=True)
    shopcard = models.IntegerField(max_length=40, null=False, blank=True)

