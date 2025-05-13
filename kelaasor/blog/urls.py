from django.urls import path
from .views import NewBlog


urlpatterns = [
    path('add-blog', NewBlog.as_view()),
]
