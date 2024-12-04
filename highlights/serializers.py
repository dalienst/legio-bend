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

    def validate(self, attrs):
        # Extract user from request context
        user = self.context["request"].user

        # Check if a highlight with the same parameters already exists
        bible_version = attrs.get("bible_version")
        bible_id = attrs.get("bible_id")
        chapter_id = attrs.get("chapter_id")
        verse_number = attrs.get("verse_number")

        if Highlight.objects.filter(
            user=user,
            bible_version=bible_version,
            bible_id=bible_id,
            chapter_id=chapter_id,
            verse_number=verse_number,
        ).exists():
            raise serializers.ValidationError(
                "A highlight for this verse already exists."
            )

        return attrs
