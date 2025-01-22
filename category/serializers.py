from rest_framework import serializers

from category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """
    - Category Serializer
    """

    author = serializers.CharField(source="author.email", read_only=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "description",
            "position",
            "author",
            "created_at",
            "updated_at",
            "slug",
            "reference",
        )
