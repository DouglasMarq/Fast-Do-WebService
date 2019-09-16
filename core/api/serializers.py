from rest_framework.serializers import ModelSerializer
from core.models import Anotation

class AnotationSerializer(ModelSerializer):
    class Meta:
        model = Anotation
        fields=('id', 'name', 'description', 'date')
