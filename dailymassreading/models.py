from django.db import models

from accounts.abstracts import TimeStampedModel, UniversalIdModel, ReferenceSlugModel


class DailyMassReading(TimeStampedModel, UniversalIdModel, ReferenceSlugModel):
    title = models.CharField(max_length=2555)
    lectionary = models.CharField(max_length=255)
    reading_one = models.CharField(max_length=255)
    reading_one_text = models.TextField()
    psalm = models.CharField(max_length=255)
    responsorial_psalm = models.TextField()
    reading_two = models.CharField(max_length=255, blank=True, null=True)
    reading_two_text = models.TextField(blank=True, null=True)
    alleluia = models.CharField(max_length=255, blank=True, null=True)
    alleluia_text = models.TextField(blank=True, null=True)
    gospel = models.CharField(max_length=255)
    gospel_text = models.TextField()

    class Meta:
        verbose_name = "Daily Mass Reading"
        verbose_name_plural = "Daily Mass Readings"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
