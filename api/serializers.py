from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Client, Project


#For user serializers Class.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

#Project serializer Class.
class ProjectSerializer(serializers.ModelSerializer):
    # client = serializers.CharField(source='client.client_name', read_only=True)
    users = UserSerializer(many=True)

    class Meta:
        model = Project
        fields = ('id', 'project_name', 'client', 'users', 'created_at', 'created_by')


#for client serializer Class
class ClientSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True,read_only=True)

    class Meta:
        model = Client
        fields = ('id', 'client_name', 'projects', 'created_at', 'created_by')

