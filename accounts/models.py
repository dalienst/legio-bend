from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from datetime import date

from accounts.abstracts import UniversalIdModel, ReferenceSlugModel, TimeStampedModel
from cloudinary.models import CloudinaryField


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save()
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_verified", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        if extra_fields.get("is_active") is not True:
            raise ValueError("Superuser must have is_active=True.")
        if extra_fields.get("is_verified") is not True:
            raise ValueError("Superuser must have is_verified=True.")

        return self._create_user(email, password, **extra_fields)


class User(
    AbstractBaseUser,
    PermissionsMixin,
    UniversalIdModel,
    TimeStampedModel,
    ReferenceSlugModel,
):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    avatar = CloudinaryField("profiles", blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    last_streak_date = models.DateField(null=True, blank=True)
    current_streak_count = models.PositiveIntegerField(default=0)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]

    objects = UserManager()

    def __str__(self):
        return self.email

    def update_streak(self):

        today = date.today()
        if not self.last_streak_date:
            # If no date exists, set today's date and increment the streak count
            self.last_streak_date = today
            self.current_streak_count = 1
        elif self.last_streak_date == today:
            # Already recorded for today, do nothing
            return
        elif (today - self.last_streak_date).days == 1:
            # The last streak was yesterday, increment the streak count
            self.current_streak_count += 1
            self.last_streak_date = today
        else:
            # The streak was broken; reset the streak count
            self.current_streak_count = 1
            self.last_streak_date = today

        self.save()


class DeletionRequest(UniversalIdModel, TimeStampedModel, ReferenceSlugModel):
    email = models.EmailField()
    reason = models.TextField()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Deletion Request"
        verbose_name_plural = "Deletion Requests"
        ordering = ["-created_at"]
