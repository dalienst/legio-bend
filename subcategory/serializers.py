from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from subcategory.models import Subcategory
from category.models import Category


class SubcategorySerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field="reference"
    )
    name = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=Subcategory.objects.all())],
        max_length=255,
    )

    class Meta:
        model = Subcategory
        fields = (
            "id",
            "name",
            "category",
            "description",
            "position",
            "tod",
            "created_at",
            "updated_at",
            "slug",
            "reference",
        )
