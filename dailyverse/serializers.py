from rest_framework import serializers

from dailyverse.models import DailyVerse


class DailyVerseSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.email", read_only=True)
    image = serializers.ImageField(use_url=True, required=False)

    class Meta:
        model = DailyVerse
        fields = (
            "id",
            "verse_text",
            "verse_reference",
            "active_date",
            "image",
            "author",
            "created_at",
            "updated_at",
            "slug",
            "reference",
        )

    def validate(self, attrs):
        """
        1. Ensure only one instance per day. There can only be one daily verse per date.
        """
        active_date = attrs.get("active_date")
        if active_date:
            # Check if there is already a DailyVerse for the same date
            existing_verse = DailyVerse.objects.filter(active_date=active_date).exclude(
                id=self.instance.id if self.instance else None
            )
            if existing_verse.exists():
                raise serializers.ValidationError(
                    {"active_date": "A daily verse already exists for this date."}
                )

        return attrs
