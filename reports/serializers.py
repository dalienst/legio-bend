from rest_framework import serializers

from reports.models import Report


class ReportSerializer(serializers.ModelSerializer):
    """
    Report serializer
    """

    report_type = serializers.CharField(max_length=255)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()

    class Meta:
        model = Report
        fields = (
            "id",
            "report_type",
            "title",
            "description",
            "created_at",
            "updated_at",
            "slug",
            "reference",
        )
