from django.urls import path
from bootcamp.views import LsBootcamps,NewBootcamp

urlpatterns = [
    path('ls-bootcamps', LsBootcamps.as_view()),
    path('new-bootcamp', NewBootcamp.as_view()),
]
