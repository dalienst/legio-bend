from django.db import models

from category.models import Category
from accounts.abstracts import TimeStampedModel, UniversalIdModel, ReferenceSlugModel


class Subcategory(UniversalIdModel, TimeStampedModel, ReferenceSlugModel):
    """
    Kitap lemo subcategory
    - Morning Prayers
    """

    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="subcategories"
    )
    description = models.TextField(blank=True, null=True)
    position = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Subcategory"
        verbose_name_plural = "Subcategories"
        ordering = ["position", "-created_at"]

    def __str__(self):
        return self.name
