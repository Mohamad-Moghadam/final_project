import os
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.conf import settings
from .models import Ticket


@receiver(pre_save, sender=Ticket)
def create_attachment_folder(sender, instance, **kwargs):
    if instance.attachment:
        upload_dir = os.path.join(settings.MEDIA_ROOT, 'attachments')
        os.makedirs(upload_dir, exist_ok=True)
