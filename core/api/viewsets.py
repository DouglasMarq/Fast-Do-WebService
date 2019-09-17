from rest_framework.viewsets import ModelViewSet
from core.models import anotation
from .serializers import anotationSerializer
from rest_framework.permissions import IsAuthenticated


class AnotationViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = anotation.objects.all()
    serializer_class = anotationSerializer