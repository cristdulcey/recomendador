from rest_framework import serializers

from services.models import Category, Service


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "name"
        )


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        exclude = (
            "description", "photo", "category",
        )