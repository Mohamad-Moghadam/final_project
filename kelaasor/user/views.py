from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User, Group
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, DestroyAPIView
from rest_framework.permissions import BasePermission, AllowAny, IsAuthenticated
from user.serializers import UserSerializer
from rest_framework.views import APIView
from user.permissions import IsHeadmaster, IsTechnician
from kavenegar import *
from django.conf import settings
from django.http import HttpResponse


class NewHeadmaster(CreateAPIView):
    permission_classes= [IsHeadmaster]
    queryset= User.objects.all()
    serializer_class= UserSerializer
    def perform_create(self, serializer):
        user= serializer.save()
        user.is_superuser= True
        user.is_staff= True
        headmaster_group= Group.objects.get(name= 'Headmaster')
        user.groups.add(headmaster_group)
        user.save()

class ListHeadmasters(ListAPIView):
    permission_classes= [IsHeadmaster]
    queryset= User.objects.filter(is_superuser= True)
    serializer_class= UserSerializer


class DeleteHeadmaster(DestroyAPIView):
    permission_classes= [IsHeadmaster]
    queryset= User.objects.filter(is_superuser= True)
    serializer_class= UserSerializer

class RetrieveHeadmaster(RetrieveAPIView):
    permission_classes= [IsHeadmaster]
    queryset= User.objects.filter(is_superuser= True)
    serializer_class= UserSerializer

class NewTech(CreateAPIView):
    permission_classes= [IsHeadmaster]
    queryset= User.objects.all()
    serializer_class= UserSerializer

    def perform_create(self, serializer):
        user= serializer.save()
        user.is_staff= True
        technician_group= Group.objects.get(name= 'Technicians')
        user.groups.add(technician_group)
        user.save()

class DelTech(DestroyAPIView):
    permission_classes= [IsHeadmaster]
    queryset= User.objects.filter(is_staff= True)
    serializer_class= UserSerializer

class LsTech(ListAPIView):
    permission_classes= [IsHeadmaster]
    queryset= User.objects.filter(is_staff= True, is_superuser= False)
    serializer_class= UserSerializer

class NewUser(CreateAPIView):
    permission_classes= [AllowAny]
    queryset= User.objects.all()
    serializer_class= UserSerializer

    def perform_create(self, serializer):
        user= serializer.save()
        user.is_active= True
        user.save()

class LogIn(APIView):
    permission_classes= [IsAuthenticated]

    def post(self, request):
        try:
            api= KavenegarAPI(settings.KAVENEGAR_API_KEY)
            params= {'sender': '2000660110', 'receptor': request.user.username, 'message' :'به کلاسور خوش آمدید!' }
            api.sms_send(params)
        except APIException as e:
            return HttpResponse(f"API Exception: {e}")


        return render(request, 'user_panel/user_panel.html', {'user': request.user})