from django.db import models

from accounts.abstracts import UniversalIdModel, TimeStampedModel, ReferenceSlugModel


class Report(UniversalIdModel, TimeStampedModel, ReferenceSlugModel):
    """
    Report bugs or suggest new features
    """

    report_type = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_solved = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Report"
        verbose_name_plural = "Reports"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
