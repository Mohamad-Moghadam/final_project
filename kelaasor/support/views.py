from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from support.models import Ticket, ResponseTicket
from support.serializers import TicketSerializer, ResponseTicketSerializer
from user.permissions import IsTechnician

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