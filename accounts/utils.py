import string
import secrets

from django.core.mail import send_mail
from django.template.loader import render_to_string
from datetime import datetime
from legiobend.settings import EMAIL_USER
import logging

logger = logging.getLogger(__name__)


def generate_slug():
    characters = string.ascii_letters + string.digits
    random_string = "".join(secrets.choice(characters) for _ in range(16))
    return random_string


def generate_reference():
    characters = string.ascii_letters + string.digits
    random_string = "".join(secrets.choice(characters) for _ in range(10))
    return random_string.upper()


def generate_code():
    characters = string.digits
    random_string = "".join(secrets.choice(characters) for _ in range(6))
    return random_string


def send_verification_email(user, verification_code):
    """
    A function to send a verification email
    """
    current_year = datetime.now().year
    email_body = render_to_string(
        "account_verification.html",
        {
            "user": user,
            "verification_code": verification_code,
            "current_year": current_year,
        },
    )

    send_mail(
        subject="Verify your account",
        message="",
        from_email=EMAIL_USER,
        recipient_list=[user.email],
        fail_silently=False,
        html_message=email_body,
    )


def send_password_reset_email(user, verification_code):
    """
    A function to send a password reset email
    """
    current_year = datetime.now().year
    email_body = render_to_string(
        "password_reset.html",
        {
            "user": user,
            "verification_code": verification_code,
            "current_year": current_year,
        },
    )

    send_mail(
        subject="Reset your password",
        message="",
        from_email=EMAIL_USER,
        recipient_list=[user.email],
        fail_silently=False,
        html_message=email_body,
    )


def send_account_deletion_request_email(email, deletion_request):
    """
    A function to alert the user that a deletion request has been made
    """
    try:
        current_year = datetime.now().year
        email_body = render_to_string(
            "account_deletion_request.html",
            {
                "email": email,
                "deletion_request": deletion_request,
                "reference": deletion_request.reference,
                "current_year": current_year,
            },
        )

        send_mail(
            subject="Account Deletion Request",
            message="",
            from_email=EMAIL_USER,
            recipient_list=[email],
            fail_silently=False,
            html_message=email_body,
        )
    except Exception as e:
        logger.error(f"Failed to send account deletion email: {e}")
        raise


def send_admin_email_on_account_deletion(email, deletion_request):
    """
    A function to alert the admin that a user has requested account deletion
    """
    try:
        current_year = datetime.now().year
        email_body = render_to_string(
            "admin_account_deletion_request.html",
            {
                "email": email,
                "deletion_request": deletion_request,
                "reference": deletion_request.reference,
                "current_year": current_year,
            },
        )

        send_mail(
            subject="Account Deletion Request",
            message="",
            from_email=EMAIL_USER,
            recipient_list=[EMAIL_USER],
            fail_silently=False,
            html_message=email_body,
        )
    except Exception as e:
        logger.error(f"Failed to send account deletion email: {e}")
        raise
    