from django.db import models

from accounts.abstracts import UniversalIdModel, TimeStampedModel, ReferenceSlugModel


class EarlyAccess(UniversalIdModel, TimeStampedModel, ReferenceSlugModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField()
    contact = models.CharField(max_length=30, null=True, blank=True)
    status = models.CharField(max_length=255, default="Pending")

    class Meta:
        verbose_name = "Early Access"
        verbose_name_plural = "Early Access Requests"
        ordering = ["-created_at"]

    def __str__(self):
        return self.email
