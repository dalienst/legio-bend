from rest_framework import serializers

from highlights.models import Highlight


class HighlightSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.email", read_only=True)

    class Meta:
        model = Highlight
        fields = (
            "id",
            "user",
            "bible_version",
            "bible_id",
            "chapter_id",
            "chapter",
            "verse_number",
            "color",
            "text",
            "created_at",
            "updated_at",
            "slug",
            "reference",
        )
