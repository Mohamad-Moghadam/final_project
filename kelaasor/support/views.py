from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from support.models import Ticket, ResponseTicket
from support.serializers import TicketSerializer, ResponseTicketSerializer, TicketAndResponseSerializer
from user.permissions import IsTechnician
from itertools import chain


class SendTicket(CreateAPIView):
    permission_classes= [IsAuthenticated]
    queryset= Ticket.objects.all()
    serializer_class= TicketSerializer
    
    def perform_create(self, serializer):
        serializer.save(user= self.request.user)

class Response(CreateAPIView):
    permission_classes= [IsTechnician]
    queryset= ResponseTicket.objects.all()
    serializer_class= ResponseTicketSerializer

class MyTickets(ListAPIView):
    permission_classes= [IsAuthenticated]

    def get_queryset(self):
        user= self.request.user
        tickets= Ticket.objects.filter(user= user)
        response= ResponseTicket.objects.filter(question__in= tickets)
        return list(chain(tickets, response))
    
    def get_serializer_class(self):
        return TicketAndResponseSerializer