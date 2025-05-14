from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView
from user.permissions import IsTechnician, IsHeadmaster
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.permissions import AllowAny


class NewBlog(CreateAPIView):
    permission_classes= [IsTechnician]
    queryset= Blog.objects.all()
    serializer_class= BlogSerializer

    def perform_create(self, serializer):
        serializer.save(author= self.request.user)


class PublishedBlogs(ListAPIView):
    permission_classes= [AllowAny]
    queryset= Blog.objects.filter(status= 'published')
    serializer_class= BlogSerializer


class ControllBlogs(ListAPIView):
    permission_classes= [IsHeadmaster]
    queryset= Blog.objects.all()
    serializer_class= BlogSerializer


class EditBlog(UpdateAPIView):
    permission_classes= [IsTechnician]
    serializer_class= BlogSerializer

    def get_queryset(self):
        return Blog.objects.filter(author= self.request.user)
