from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'username', 'groups', 'user_permissions')
        # fields = '__all__'
