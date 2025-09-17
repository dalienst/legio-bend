from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

from accounts.abstracts import TimeStampedModel, UniversalIdModel, ReferenceSlugModel

User = get_user_model()


class Teaching(TimeStampedModel, UniversalIdModel, ReferenceSlugModel):
    title = models.CharField(max_length=2550)
    location = models.CharField(max_length=2550, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name="teachings")
    identity = models.CharField(max_length=2550, blank=True, null=True, unique=True)

    class Meta:
        verbose_name = "Teaching"
        verbose_name_plural = "Teachings"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.identity:
            self.identity = slugify(f"{self.title}-{self.reference}")
        return super().save(*args, **kwargs)
