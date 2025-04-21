from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, DestroyAPIView
from rest_framework.permissions import BasePermission, AllowAny
from user.serializers import UserSerializer
from user.models import HeadMaster

class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser

class IsTech(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['PATCH', 'PUT', 'GET', 'DELETE', 'POST']:
            if request.user.is_staff or request.user.is_superuser:
                return False
        else:
            return True

class NewHeadmaster(CreateAPIView):
    permission_classes= [IsSuperUser]
    queryset= User
    serializer_class= UserSerializer
    def perform_create(self, serializer):
        user= serializer.save()
        user.is_superuser= True
        user.is_staff= True
        user.save()
    def __str__(self):
        print(self.user)

class SignUp(CreateAPIView):
    permission_classes= [AllowAny]
    queryset= User
    serializer_class= UserSerializer

class ListHeadmasters(ListAPIView):
    permission_classes= [IsSuperUser]
    queryset= User.objects.filter(is_superuser= True)
    serializer_class= UserSerializer


class DeleteHeadmaster(DestroyAPIView):
    permission_classes= [IsSuperUser]
    queryset= User.objects.filter(is_superuser= True)
    serializer_class= UserSerializer

class RetrieveHeadmaster(RetrieveAPIView):
    permission_classes= [IsSuperUser]
    queryset= User.objects.filter(is_superuser= True)
    serializer_class= UserSerializer

class NewTech(CreateAPIView):
    permission_classes= [IsSuperUser]
    queryset= User.objects.all()
    serializer_class= UserSerializer

    def perform_create(self, serializer):
        user= serializer.save()
        user.is_staff= True
        user.save()
    def __str__(self):
        return f"{self.user}"

class DelTech(DestroyAPIView):
    permission_classes= [IsSuperUser]
    queryset= User.objects.filter(is_staff= True)
    serializer_class= UserSerializer

class LsTech(ListAPIView):
    permission_classes= [IsSuperUser]
    queryset= User.objects.filter(is_staff= True, is_superuser= False)
    serializer_class= UserSerializer