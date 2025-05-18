from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from support.models import Ticket, ResponseTicket
from support.serializers import TicketSerializer, ResponseTicketSerializer, TicketAndResponseSerializer
from user.permissions import IsTechnician, IsHeadmaster
from itertools import chain
from .tasks import send_informing_SMS
from django.contrib.auth.models import Group
from django.conf import settings
from django.core.mail import send_mail



class SendTicket(CreateAPIView):
    permission_classes= [IsAuthenticated]
    queryset= Ticket.objects.all()
    serializer_class= TicketSerializer
    
    def perform_create(self, serializer):
        ticket= serializer.save(user= self.request.user)
        technicians = Group.objects.get(name='Technicians').user_set.all()
        emails = [tech.username for tech in technicians if tech.username]

        if emails:
            send_mail(
            subject='تیکت جدید',
            message=f'یک تیکت جدید توسط {ticket.user} ثبت شده است.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=emails,
            fail_silently=False,
    )

class Response(CreateAPIView):
    permission_classes= [IsTechnician]
    queryset= ResponseTicket.objects.all()
    serializer_class= ResponseTicketSerializer

    def perform_create(self, serializer):
        response= serializer.save()
        phone_number= response.question.user
        send_informing_SMS.delay(phone_number)

class MyTickets(ListAPIView):
    permission_classes= [IsAuthenticated]

    def get_queryset(self):
        user= self.request.user
        tickets= Ticket.objects.filter(user= user)
        response= ResponseTicket.objects.filter(question__in= tickets)
        return list(chain(tickets, response))
    
    def get_serializer_class(self):
        return TicketAndResponseSerializer

class ListTickets(ListAPIView):
    permission_classes= [IsHeadmaster]
    queryset= Ticket.objects.all()
    serializer_class= TicketAndResponseSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context