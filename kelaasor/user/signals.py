from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.apps import apps


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def assign_user_to_groups(sender, instance, created, **kwargs):
    if not created:
        return

    group_name = None

    if instance.is_superuser:
        group_name = 'Headmaster'
    elif instance.is_staff and not instance.is_superuser:
        group_name = 'Technicians'

    if not group_name:
        return

    group, _ = Group.objects.get_or_create(name=group_name)
    permission_codenames = settings.USER_GROUP_PERMISSIONS.get(group_name, [])

    permissions = Permission.objects.filter(codename__in=permission_codenames)

    for perm in permissions:
        if not group.permissions.filter(id=perm.id).exists():
            group.permissions.add(perm)

    instance.groups.add(group)
    instance.save()