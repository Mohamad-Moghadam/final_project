"""from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def add_superuser_to_the_headmaster(sender, instance, created, **kwargs):
    if created:
        if instance.is_superuser:
            group = Group.objects.get_or_create(name='Headmaster')
            instance.groups.add(group)"""