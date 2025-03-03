from django.core.mail import send_mail
from django.template.loader import render_to_string
from datetime import datetime
from legiobend.settings import EMAIL_USER
import logging

logger = logging.getLogger(__name__)


def notify_admin_on_early_access_request(email, early_access_request):
    try:
        current_year = datetime.now().year
        email_body = render_to_string(
            "admin_early_access_request.html",
            {
                "email": email,
                "early_access_request": early_access_request,
                "reference": early_access_request.reference,
                "current_year": current_year,
            },
        )

        send_mail(
            subject="Early Access Request",
            message="",
            from_email=EMAIL_USER,
            recipient_list=[EMAIL_USER],
            fail_silently=False,
            html_message=email_body,
        )
    except Exception as e:
        logger.error(f"Failed to send early access request email: {e}")
        raise


def notify_user_on_early_access_request(email, early_access_request):
    try:
        current_year = datetime.now().year
        email_body = render_to_string(
            "early_access_request.html",
            {
                "email": email,
                "early_access_request": early_access_request,
                "reference": early_access_request.reference,
                "current_year": current_year,
            },
        )

        send_mail(
            subject="Early Access Request",
            message="",
            from_email=EMAIL_USER,
            recipient_list=[email],
            fail_silently=False,
            html_message=email_body,
        )

    except Exception as e:
        logger.error(f"Failed to send early access request email: {e}")
        raise
