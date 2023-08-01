from django.apps import AppConfig


class AppuserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appUser'
    def ready(self):
        import appUser.signals
