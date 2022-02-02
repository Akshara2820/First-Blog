from django.apps import AppConfig
from django.http import HttpResponse


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'


