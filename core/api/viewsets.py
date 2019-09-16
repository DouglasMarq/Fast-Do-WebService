from rest_framework.viewsets import ModelViewSet
from core.models import anotation
from .serializers import anotationSerializer


class AnotationViewSet(ModelViewSet):
    queryset = anotation.objects.all()
    serializer_class = anotationSerializer