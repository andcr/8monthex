from django.db import models
import django.utils.timezone
class Product(models.Model):
    name = models.CharField(max_length=30, null=False, blank=True)
    price = models.IntegerField(null=False, blank=True)
    date = models.DateField(null=False, blank=True, )


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    shopcard = models.IntegerField(null=True)
    def __str__(self):
        return self.name
    def save_customer(self):
        self.save()