from rest_framework.serializers import ModelSerializer
from support.models import Ticket, ResponseTicket


class TicketSerializer(ModelSerializer):
    class Meta:
        model= Ticket
        fields= '__all__'
        read_only_fields= ['user']

class ResponseTicketSerializer(ModelSerializer):
    class Meta:
        model= ResponseTicket
        fields= '__all__'