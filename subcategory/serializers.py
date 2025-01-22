from rest_framework import serializers

from subcategory.models import Subcategory
from category.models import Category


class SubcategorySerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field="slug"
    )

    class Meta:
        model = Subcategory
        fields = (
            "id",
            "name",
            "category",
            "description",
            "position",
            "author",
            "created_at",
            "updated_at",
            "slug",
            "reference",
        )

    
