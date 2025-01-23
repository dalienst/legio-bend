from django.db import models

from accounts.abstracts import TimeStampedModel, UniversalIdModel, ReferenceSlugModel
from subcategory.models import SubCategory


class Prayer(TimeStampedModel, UniversalIdModel, ReferenceSlugModel):
    title = models.CharField(max_length=255)
    subcategory = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, related_name="prayers"
    )
    content = models.TextField()
    purpose = models.CharField(max_length=255, blank=True, null=True)
    is_public = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Prayer"
        verbose_name_plural = "Prayers"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
