from django.apps import AppConfig


class CarparkConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "carpark"

    def ready(self):
        import carpark.signals
