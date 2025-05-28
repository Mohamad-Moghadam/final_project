from django.urls import path
from bootcamp.views import LsBootcamps,NewBootcamp, SignInBootCamp, DelBootcamp, EditBootcamp, EnrollmentApproval, MyBootcamps

urlpatterns = [
    path('ls-bootcamps', LsBootcamps.as_view()),
    path('new-bootcamp', NewBootcamp.as_view()),
    path('del-bootcamp/<int:pk>', DelBootcamp.as_view()),
    path('edit-bootcamp/<int:pk>', EditBootcamp.as_view()),
    path('enrollment-approval/<int:pk>', EnrollmentApproval.as_view()),
    path('my-bootcamps', MyBootcamps.as_view()),
    path('sign-in-bootcamp', SignInBootCamp.as_view()),
]