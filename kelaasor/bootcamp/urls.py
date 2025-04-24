from django.urls import path
from bootcamp.views import LsBootcamps

urlpatterns = [
    path('ls-bootcamps', LsBootcamps.as_view()),
]
