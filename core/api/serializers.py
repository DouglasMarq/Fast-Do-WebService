from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from core.models import anotation, User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

class anotationSerializer(ModelSerializer):
    class Meta:
        model = anotation
        fields=('id', 'name', 'description', 'date')
        
class UserSerializer(ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            max_length=32,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')