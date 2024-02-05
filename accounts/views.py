from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from rest_framework.decorators import api_view
from rest_framework.response import Response

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, World!'})
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .serializers import *
from rest_framework import generics
from .models import Customer
from .serializers import CustomerSerializer


class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


@api_view(['POST'])
def createproduct(price, date, name, category, request):
    product_serializer_data = ProductSerializer(data=request.data)
    if product_serializer_data.is_valid():
        product_serializer_data.save()
        status_code = status.HTTP_201_CREATED
        return Response({"message": "Product Added Sucessfully", "status": status_code})
    else:
        status_code = status.HTTP_400_BAD_REQUEST
        return Response({"message": "please fill the datails", "status": status_code})


@api_view(['DELETE'])
def destroy(self, request, *args, **kwargs):
    product_data = Product.objects.filter(id=kwargs['pk'])
    if product_data:
        product_data.delete()
        status_code = status.HTTP_201_CREATED
        return Response({"message": "Product delete Sucessfully", "status": status_code})
    else:
        status_code = status.HTTP_400_BAD_REQUEST
        return Response({"message": "Product data not found", "status": status_code})
class GetMethod(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@api_view(['GET'])


def list(self, request, *args, **kwargs):
    data = list(Product.objects.all().values())
    return Response(data)
@api_view(['GET'])
def update(self, request, *args, **kwargs):
    product_details = Product.objects.get(id=kwargs['pk'])
    product_serializer_data = ProductSerializer(
        product_details, data=request.data, partial=True)
    if product_serializer_data.is_valid():
        product_serializer_data.save()
        status_code = status.HTTP_201_CREATED
        return Response({"message": "Product Update Sucessfully", "status": status_code})
    else:
        status_code = status.HTTP_400_BAD_REQUEST
        return Response({"message": "Product data Not found", "status": status_code})