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

    def perform_update(self, serializer):
        user= self.request.user
        wallet = user.wallet
        bootcamp = serializer.instance

        if wallet.balance >= bootcamp.price and bootcamp.enrollment_status == True and user not in bootcamp.students.all():
            bootcamp.students.add(user)
            wallet.balance -= bootcamp.price
            wallet.save()
            serializer.save()
            return JsonResponse({"message": "student added to the bootcamp"})
        
        else:
            return JsonResponse({"message": "not enough balance or enrollment is closed for you."})
