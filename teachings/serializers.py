from rest_framework import serializers

from teachings.models import Teaching


class TeachingSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.email", read_only=True)

    class Meta:
        model = Teaching
        fields = (
            "author",
            "title",
            "location",
            "date",
            "content",
            "identity",
            "created_at",
            "updated_at",
            "slug",
            "reference",
        )
