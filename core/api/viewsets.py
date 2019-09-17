from rest_framework.viewsets import ModelViewSet
from core.models import anotation, register
from .serializers import anotationSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView


class AnotationViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = anotation.objects.all()
    serializer_class = anotationSerializer

class RegisterViewSet(ModelViewSet):
    model = register
    queryset = anotation.objects.all()
    serializer_class = UserSerializer