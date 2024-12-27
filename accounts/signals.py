from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import DeletionRequest

from accounts.utils import (
    send_account_deletion_request_email,
    send_admin_email_on_account_deletion,
)
import logging

logger = logging.getLogger(__name__)


@receiver(post_save, sender=DeletionRequest)
def handle_deletion_request(sender, instance, created, **kwargs):
    if created:
        try:
            send_account_deletion_request_email(
                email=instance.email, deletion_request=instance
            )
        except Exception as e:
            logger.error(f"Error sending user email: {e}")

        try:
            send_admin_email_on_account_deletion(
                email=instance.email, deletion_request=instance
            )
        except Exception as e:
            logger.error(f"Error sending admin email: {e}")
