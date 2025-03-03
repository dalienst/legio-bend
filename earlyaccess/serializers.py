from rest_framework import serializers

from earlyaccess.models import EarlyAccess


class EarlyAccessSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = EarlyAccess
        fields = (
            "id",
            "name",
            "email",
            "contact",
            "status",
            "reference",
            "slug",
            "created_at",
            "updated_at",
        )
