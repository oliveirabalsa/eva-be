from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User, Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        user.save()
        return user

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__' 
        read_only_fields = ('created_at', 'updated_at')  # Exemplo: Tornar campos somente leitura

    def create(self, validated_data):
        # Personalizar a criação da tarefa (opcional)
        task = Task.objects.create(**validated_data) 
        return task