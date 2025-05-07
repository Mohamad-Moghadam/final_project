from django.urls import path
from support.views import SendTicket, Response, MyTickets

urlpatterns = [
    path('send-ticket', SendTicket.as_view()),
    path('send-response', Response.as_view()),
    path('my-tickets', MyTickets.as_view()),
]
