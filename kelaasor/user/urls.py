from django.urls import path
from user.views import NewHeadmaster, ListHeadmasters, DeleteHeadmaster, RetrieveHeadmaster, NewTech, DelTech, LsTech, NewUser, LogIn, ListAllUsers, ForgetPassword
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('get-token', TokenObtainPairView.as_view()),
    path('new-headmaster', NewHeadmaster.as_view()),
    path('ls-headmasters', ListHeadmasters.as_view()),
    path('del-headmaster/<int:pk>', DeleteHeadmaster.as_view()),
    path('retrieve-headmaster/<int:pk>', RetrieveHeadmaster.as_view()),
    path('new-tech', NewTech.as_view()),
    path('del-tech/<int:pk>', DelTech.as_view()),
    path('ls-techs', LsTech.as_view()),
    path('sign-up', NewUser.as_view()),
    path('log-in', LogIn.as_view()),
    path('ls-users', ListAllUsers.as_view()),
    path('forget-password', ForgetPassword.as_view()),
]
