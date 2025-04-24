from rest_framework.serializers import ModelSerializer
from bootcamp.models import BootCamps

class BootcampSerializer(ModelSerializer):
    class Meta:
        model= BootCamps
        fields= '__all__'