from rest_framework.viewsets import ModelViewSet
from core.models import Anotation
from .serializers import AnotationSerializer


class AnotationViewSet(ModelViewSet):
    queryset = Anotation.objects.all()
    serializer_class = AnotationSerializer