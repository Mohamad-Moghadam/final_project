from rest_framework.serializers import ModelSerializer
from bootcamp.models import BootCamps, BootcampRequest

class BootcampSerializer(ModelSerializer):
    class Meta:
        model= BootCamps
        fields= '__all__'

class BootcampRequestSerializer(ModelSerializer):
    class Meta:
        model= BootcampRequest
        fields= '__all__'
        read_only_fields = ['user']