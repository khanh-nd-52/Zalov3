from django.contrib.auth import get_user_model
from rest_framework import serializers
# from core.models import Post, Comment
# from django.core.paginator import Paginator
# from rest_framework.settings import api_settings


class RegisterUserSerializer(serializers.ModelSerializer):
    """Serializer for creating a new user account"""

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'fullname')
        extra_kwargs = {'password': {'write_only': True,
                                     'min_length': 6},
                        'username': {'min_length': 10}}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)