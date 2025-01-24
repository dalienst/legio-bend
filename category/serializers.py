from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from category.models import Category
from subcategory.serializers import SubcategorySerializer


class CategorySerializer(serializers.ModelSerializer):
    """
    - Category Serializer
    """

    author = serializers.CharField(source="author.email", read_only=True)
    name = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=Category.objects.all())],
        max_length=255,
    )
    subcategories = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "description",
            "position",
            "author",
            "period",
            "subcategories",
            "created_at",
            "updated_at",
            "slug",
            "reference",
        )
