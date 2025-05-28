from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from bootcamp.models import BootCamps, BootcampRequest
from bootcamp.serializers import BootcampSerializer, BootcampRequestSerializer
from user.permissions import IsHeadmaster, IsTechnician
from rest_framework.permissions import IsAuthenticated
from .models import BootCamps
from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.contrib.auth.models import Group, User
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from transaction.models import Wallet



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


class SignInBootCamp(CreateAPIView):
    permission_classes= [IsAuthenticated]
    queryset= BootcampRequest.objects.all()
    serializer_class= BootcampRequestSerializer

    def perform_create(self, serializer):
        bootcamp_request = serializer.save(user = self.request.user)
        technicians = Group.objects.get(name='Technicians').user_set.all()
        emails = [tech.username for tech in technicians]

        if emails:
            send_mail(
                subject = "درخاست جدید ثبت نام در بوتکمپ",
                message = f"یک درخاست جدید ثبت نام در باتکمپ ثبت شده است. لطفا درخاست را بررسی کنید.",
                from_email = settings.EMAIL_HOST_USER,
                recipient_list = emails,
                fail_silently = False,
            )

class EnrollmentApproval(UpdateAPIView):
    permission_classes= [IsTechnician]
    queryset= BootCamps.objects.all()
    serializer_class= BootcampSerializer

    def update(self, request, *args, **kwargs):
        username = request.data.get("username")
        if not username:
            return Response({"message": "Username is required."}, status=status.HTTP_400_BAD_REQUEST)

        user = get_object_or_404(User, username=username)
        wallet, _ = Wallet.objects.get_or_create(user=user)

        bootcamp = self.get_object()
        already_enrolled = bootcamp.students.filter(pk=user.pk).exists()

        if wallet.balance >= bootcamp.price and bootcamp.enrollment_status and not already_enrolled:
            bootcamp.students.add(user)
            wallet.balance -= bootcamp.price
            wallet.save()
            return Response({"message": f"{username} was enrolled successfully."})
        else:
            return Response({"message": "Not enough balance, enrollment is closed, or user is already enrolled."}, status=status.HTTP_400_BAD_REQUEST)

class MyBootcamps(ListAPIView):
    permission_classes= [IsAuthenticated]
    serializer_class= BootcampSerializer

    def get_queryset(self):
        user= self.request.user
        return BootCamps.objects.filter(students__in=[user])
