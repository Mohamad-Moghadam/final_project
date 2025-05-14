from django.urls import path
from .views import NewBlog, PublishedBlogs, ControllBlogs


urlpatterns = [
    path('add-blog', NewBlog.as_view()),
    path('show-blogs', PublishedBlogs.as_view()),
    path('controll-blogs', ControllBlogs.as_view()),
]
