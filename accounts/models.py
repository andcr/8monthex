from django.db import models

# Create your models here.

# class Customer(models.Model):
#     name = models.CharField(max_length=30, null=True,blank=True)
#     phone = models.CharField(max_length=40,null=True, blank=True)
#     shopcard = models.IntegerField(max_length=40,null=True, blank=True)
#     spend = models.IntegerField(null=True, blank=True)

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
class Product(models.Model):
    name = models.CharField(max_length=30, null=False, blank=True)
    price = models.IntegerField(null=False, blank=True)
    date = models.DateField(null=False, blank=True, )