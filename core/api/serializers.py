from rest_framework.serializers import ModelSerializer
from core.models import anotation

class anotationSerializer(ModelSerializer):
    class Meta:
        model = anotation
        fields=('id', 'name', 'description', 'date')