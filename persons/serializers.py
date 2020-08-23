from django.contrib.auth.models import User
from persons.models import City, Client, Supervisor
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "password", "groups", "user_permissions", "is_staff", "is_active",
            "is_superuser"
        )

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            "id", "user", "city", "phone", "address",
        )

class SupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supervisor
        fields = "__all__"