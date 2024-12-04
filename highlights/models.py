from django.db import models
from django.contrib.auth import get_user_model

from accounts.abstracts import ReferenceSlugModel, UniversalIdModel, TimeStampedModel

User = get_user_model()


class Highlight(UniversalIdModel, ReferenceSlugModel, TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="highlights")
    bible_version = models.CharField(max_length=255)
    bible_id = models.CharField(max_length=255)
    chapter_id = models.CharField(max_length=255)
    chapter = models.CharField(max_length=255)
    verse_number = models.PositiveIntegerField()
    color = models.CharField(max_length=7, default="#FFFF00")
    text = models.TextField()

    class Meta:
        verbose_name = "Highlight"
        verbose_name_plural = "Highlights"
        ordering = ["verse_number"]

    def __str__(self):
        return f"{self.bible_version} {self.chapter}:{self.verse_number} - {self.text[:50]}..."
