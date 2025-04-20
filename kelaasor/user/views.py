from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import BasePermission, AllowAny
from serializers import UserSerializer

class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser

class NewHeadmaster(CreateAPIView):
    permission_classes= [IsSuperUser]
    queryset= User
    serializer_class= UserSerializer

class SignUp(CreateAPIView):
    permission_classes= [AllowAny]
    queryset= User
    serializer_class= UserSerializer

