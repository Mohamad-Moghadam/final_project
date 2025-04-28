from django.urls import path
from support.views import SendTicket

urlpatterns = [
    path('send-ticket', SendTicket.as_view()),
]
