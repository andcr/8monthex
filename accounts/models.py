from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30, null=True,blank=True)
    price = models.CharField(max_length=40,null=True, blank=True)
    quantity = models.IntegerField(blank=True, null=True)
# class Customer(models.Model):
#     name = models.CharField(max_length=30, null=True,blank=True)
#     phone = models.CharField(max_length=40,null=True, blank=True)
#     shopcard = models.IntegerField(max_length=40,null=True, blank=True)
#     spend = models.IntegerField(null=True, blank=True)
class Market(models.Model):
    name = models.CharField(max_length=30, null=True,blank=True)
    product = models.CharField(max_length=50,null=False,blank=True)
    profit = models.IntegerField(max_length=100,null=True,blank=True)
    customer = models.CharField(max_length=50,null=False,blank=True)
    date = models.DateField(null=True,blank=True)
    time = models.TimeField(null=True,blank=True)
