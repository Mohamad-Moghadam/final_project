from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    STATUS= [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    title = models.CharField(max_length=255)
    content = models.TextField()
    type = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name= 'author')
    created_at = models.DateTimeField(auto_now_add=True)
    status= models.CharField(max_length=10, choices= STATUS, default= 'draft')
