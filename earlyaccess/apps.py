from django.apps import AppConfig


class EarlyaccessConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "earlyaccess"

    def ready(self):
        import earlyaccess.signals
