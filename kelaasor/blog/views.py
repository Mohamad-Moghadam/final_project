from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from user.permissions import IsTechnician
from .models import Blog
from .serializers import BlogSerializer


class NewBlog(CreateAPIView):
    permission_classes= [IsTechnician]
    queryset= Blog.objects.all()
    serializer_class= BlogSerializer
