from django.apps import AppConfig


class CompositeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'composite'
    
    verbose_name = 'Composite Items'
