from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import DeletionRequest

from accounts.utils import send_account_deletion_request_email


@receiver(post_save, sender=DeletionRequest)
def handle_deletion_request(sender, instance, created, **kwargs):
    if created:
        send_account_deletion_request_email(
            email=instance.email, deletion_request=instance
        )
