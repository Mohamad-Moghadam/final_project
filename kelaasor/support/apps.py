from django.apps import AppConfig
import os
from django.conf import settings


class SupportConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'support'

    def ready(self):
        attachments_path = os.path.join(settings.MEDIA_ROOT, 'attachments')
        os.makedirs(attachments_path, exist_ok=True)