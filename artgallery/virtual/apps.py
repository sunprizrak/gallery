from django.apps import AppConfig


class VirtualConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'virtual'
    verbose_name = 'Выставки'
