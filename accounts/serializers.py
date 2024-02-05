from rest_framework import serializers
from .models  import*
from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
class ProductSerializer(serializers.ModelSerializer):
    class Meta():
        model = Product
        fields = "__all__"