from rest_framework import serializers

from .models import UserApplication


class UserApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserApplication
        fields = ("submitted")