from django.urls import path
from bootcamp.views import LsBootcamps,NewBootcamp, DelBootcamp, EditBootcamp, Enroll

urlpatterns = [
    path('ls-bootcamps', LsBootcamps.as_view()),
    path('new-bootcamp', NewBootcamp.as_view()),
    path('del-bootcamp/<int:pk>', DelBootcamp.as_view()),
    path('edit-bootcamp/<int:pk>', EditBootcamp.as_view()),
    path('enroll/<int:pk>', Enroll.as_view()),
]
