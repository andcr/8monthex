from django.urls import path

from .views import SignUpView
from .views import hello_world

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("hello_world/", hello_world, name="hello_world"),
]