from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def assign_user_to_groups(sender, instance, created, **kwargs):
    if not created:
        return

    if instance.is_superuser:
        group, _ = Group.objects.get_or_create(name='Headmaster')
        instance.groups.add(group)
        instance.save()

    elif instance.is_staff and not instance.is_superuser:
        group, _ = Group.objects.get_or_create(name='Technicians')
        instance.groups.add(group)
        instance.save()