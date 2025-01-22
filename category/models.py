from django.db import models
from django.contrib.auth import get_user_model

from accounts.abstracts import TimeStampedModel, UniversalIdModel, ReferenceSlugModel

User = get_user_model()


class Category(TimeStampedModel, UniversalIdModel, ReferenceSlugModel):
    """
    Kitap Lemo Category model
    - Daily Prayers
    """

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    position = models.PositiveIntegerField(default=0, help_text="Position in the list")
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="categories",
    )

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["position", "-created_at"]

    def __str__(self):
        return self.name
