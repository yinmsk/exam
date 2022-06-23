from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password", "fullname", "email"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password", "fullname", "email"]

        class UserSerializer(serializers.ModelSerializer):


class Meta:
        model = User
        fields = ["username", "password", "fullname", "email"]
        class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "password", "fullname", "email"]
