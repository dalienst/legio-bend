from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from accounts.validators import (
    validate_password_digit,
    validate_password_uppercase,
    validate_password_lowercase,
    validate_password_symbol,
)

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password = serializers.CharField(
        max_length=128,
        min_length=5,
        write_only=True,
        validators=[
            validate_password_digit,
            validate_password_uppercase,
            validate_password_symbol,
            validate_password_lowercase,
        ],
    )
    avatar = serializers.ImageField(use_url=True, required=False)

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "password",
            "first_name",
            "last_name",
            "avatar",
            "reference",
            "slug",
            "is_staff",
            "is_active",
            "created_at",
            "updated_at",
        )

    def create_user(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
