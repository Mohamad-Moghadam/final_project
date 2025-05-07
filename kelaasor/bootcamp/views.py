from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from bootcamp.models import BootCamps
from bootcamp.serializers import BootcampSerializer
from user.permissions import IsHeadmaster
from rest_framework.permissions import IsAuthenticated
from .models import BootCamps
from datetime import datetime
from django.http import JsonResponse


class LsBootcamps(ListAPIView):
    permission_classes= [AllowAny]
    queryset= BootCamps.objects.all()
    serializer_class= BootcampSerializer

class NewBootcamp(CreateAPIView):
    permission_classes= [IsHeadmaster]
    queryset= BootCamps.objects.all()
    serializer_class= BootcampSerializer

class DelBootcamp(DestroyAPIView):
    permission_classes= [IsHeadmaster]
    queryset= BootCamps.objects.all()
    serializer_class= BootcampSerializer

class EditBootcamp(UpdateAPIView):
    permission_classes= [IsHeadmaster]
    queryset= BootCamps.objects.all()
    serializer_class= BootcampSerializer


class Enroll(UpdateAPIView):
    permission_classes= [IsAuthenticated]
    queryset= BootCamps.objects.all()
    serializer_class= BootcampSerializer

    def update(self, serializer, *args, **kwargs):
        user= self.request.user
        wallet = user.wallet
        bootcamp = self.get_object()
        already_enrolled = bootcamp.students.filter(pk=user.pk).exists()

        if wallet.balance >= bootcamp.price and bootcamp.enrollment_status == True and not already_enrolled:
            bootcamp.students.add(user)
            wallet.balance -= bootcamp.price
            wallet.save()
            return JsonResponse({"message": "student was added to the bootcamp"})
        
        else:
            return JsonResponse({"message": "not enough balance or enrollment is closed for you."})


class MyBootcamps(ListAPIView):
    permission_classes= [IsAuthenticated]
    serializer_class= BootcampSerializer

    def get_queryset(self):
        user= self.request.user
        return BootCamps.objects.filter(students__in=[user])
