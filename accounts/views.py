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