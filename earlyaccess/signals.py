from django.db.models.signals import post_save
from django.dispatch import receiver
from earlyaccess.models import EarlyAccess

from earlyaccess.utils import (
    notify_admin_on_early_access_request,
    notify_user_on_early_access_request,
)

import logging

logger = logging.getLogger(__name__)


@receiver(post_save, sender=EarlyAccess)
def handle_early_access_request(sender, instance, created, **kwargs):
    if created:
        try:
            notify_admin_on_early_access_request(
                email=instance.email, early_access_request=instance
            )
        except Exception as e:
            logger.error(f"Failed to send early access request email: {e}")

        try:
            notify_user_on_early_access_request(
                email=instance.email, early_access_request=instance
            )
        except Exception as e:
            logger.error(f"Failed to send early access request email: {e}")
