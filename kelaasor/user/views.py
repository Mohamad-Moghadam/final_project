from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from serializers import UserSerializer


class SignUp(CreateAPIView):
    permission_classes= [AllowAny]
    queryset= User
    serializer_class= UserSerializer
