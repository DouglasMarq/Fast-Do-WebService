from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from core.models import anotation, register

class anotationSerializer(ModelSerializer):
    class Meta:
        model = anotation
        fields=('id', 'name', 'description', 'date')

        
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    def create(self, validated_data):
        user = register.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    class Meta:
        model = register
        # Tuple of serialized model fields (see link [2])
        fields = ( "id", "username", "password", "email")