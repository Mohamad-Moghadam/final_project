from django.urls import path
from user.views import NewHeadmaster, ListHeadmasters, DeleteHeadmaster
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('sign-up', TokenObtainPairView.as_view()),
    path('new-headmaster', NewHeadmaster.as_view()),
    path('ls-headmasters', ListHeadmasters.as_view()),
    path('del-headmaster/<int:pk>', DeleteHeadmaster.as_view()),
]
