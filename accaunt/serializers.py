from django.contrib.auth.models import User
from rest_framework import serializers

class UserRegisterationsSerializer(serializers.ModelSerializer):
    # check_password = serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

