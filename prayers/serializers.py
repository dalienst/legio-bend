from rest_framework import serializers

from prayers.models import Prayer
from subcategory.models import Subcategory


class PrayerSerializer(serializers.ModelSerializer):
    subcategory = serializers.SlugRelatedField(
        queryset=Subcategory.objects.all(), slug_field="reference"
    )
    subcategory_detail = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Prayer
        fields = (
            "id",
            "title",
            "subcategory",
            "content",
            "purpose",
            "is_public",
            "position",
            "created_at",
            "updated_at",
            "slug",
            "reference",
        )

    def get_subcategory_detail(self, obj):
        return obj.subcategory.name
