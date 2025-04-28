from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from support.models import Ticket
from support.serializers import TicketSerializer

class SendTicket(CreateAPIView):
    permission_classes= [IsAuthenticated]
    queryset= Ticket.objects.all()
    serializer_class= TicketSerializer
    
    def perform_create(self, serializer):
        serializer.save(user= self.request.user)