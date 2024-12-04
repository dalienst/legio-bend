from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField

from accounts.abstracts import TimeStampedModel, UniversalIdModel, ReferenceSlugModel

User = get_user_model()


class DailyVerse(TimeStampedModel, UniversalIdModel, ReferenceSlugModel):
    verse_text = models.TextField()
    verse_reference = models.CharField(max_length=255, help_text="e.g. John 3:16")
    active_date = models.DateField()
    image = CloudinaryField("dailyverse", blank=True, null=True)
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="dailyverses",
    )

    class Meta:
        verbose_name = "Daily Verse"
        verbose_name_plural = "Daily Verses"
        ordering = ["-active_date"]

    def __str__(self):
        return f"{self.verse_reference} - {self.active_date}"
