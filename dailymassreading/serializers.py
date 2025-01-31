from rest_framework import serializers

from dailymassreading.models import DailyMassReading


class DailyMassReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyMassReading
        fields = (
            "id",
            "title",
            "lectionary",
            "reading_one",
            "reading_one_text",
            "psalm",
            "responsorial_psalm",
            "reading_two",
            "reading_two_text",
            "alleluia",
            "alleluia_text",
            "gospel",
            "gospel_text",
            "created_at",
            "updated_at",
            "slug",
            "reference",
        )
