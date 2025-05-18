from rest_framework.serializers import ModelSerializer
from support.models import Ticket, ResponseTicket
from rest_framework import serializers


class TicketSerializer(ModelSerializer):
    class Meta:
        model= Ticket
        fields= '__all__'
        read_only_fields= ['user']

class ResponseTicketSerializer(ModelSerializer):
    class Meta:
        model= ResponseTicket
        fields= '__all__'

class TicketAndResponseSerializer(serializers.ModelSerializer):
    responses = ResponseTicketSerializer(many=True, read_only=True)
    attachment_url = serializers.SerializerMethodField()

    class Meta:
        model = Ticket
        fields = '__all__'
        read_only_fields = ['user']

    def get_attachment_url(self, obj):
        request = self.context.get('request')
        if obj.attachment:
            return request.build_absolute_uri(obj.attachment.url)
        return None