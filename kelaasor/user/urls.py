from django.urls import path
from user.views import NewHeadmaster
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('sign-up', TokenObtainPairView.as_view()),
    path('new-headmaster', NewHeadmaster.as_view())
]
