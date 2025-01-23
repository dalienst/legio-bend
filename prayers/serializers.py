from rest_framework import serializers

from prayers.models import Prayer
from subcategory.models import Subcategory


class PrayerSerializer(serializers.ModelSerializer):
    subcategory = serializers.SlugRelatedField(
        queryset=Subcategory.objects.all(), slug_field="reference"
    )

    class Meta:
        model = Prayer
        fields = (
            "id",
            "title",
            "subcategory",
            "content",
            "purpose",
            "is_public",
            "created_at",
            "updated_at",
            "slug",
            "reference",
        )
