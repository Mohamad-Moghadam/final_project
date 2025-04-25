from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from bootcamp.models import BootCamps
from bootcamp.serializers import BootcampSerializer
from user.permissions import IsHeadmaster


class LsBootcamps(ListAPIView):
    permission_classes= [AllowAny]
    queryset= BootCamps.objects.all()
    serializer_class= BootcampSerializer

class NewBootcamp(CreateAPIView):
    permission_classes= [IsHeadmaster]
    queryset= BootCamps.objects.all()
    serializer_class= BootcampSerializer