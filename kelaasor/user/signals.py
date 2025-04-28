from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def assign_user_to_groups(sender, instance, created, **kwargs):
    if not created:
        return

    if instance.is_superuser:
        group, _ = Group.objects.get_or_create(name='Headmaster')
        custom_permissions= Permission.objects.filter(codename__in= ["can_add_headmaster", "can_list_headmasters", "can_delete_headmaster", "can_retrieve_headmaster", "can_add_technician", "can_list_technicians", "can_delete_technician", "can_retrieve_technician",
        "add_bootcamp", "view_bootcamp", "delete_bootcamp", "change_bootcamp", "add_ticket", "view_ticket", "delete_ticket", "change_ticket"])

        if not group.permissions.filter(codename='can_add_headmaster').exists():
            group.permissions.add(*custom_permissions)

        instance.groups.add(group)

    elif instance.is_staff and not instance.is_superuser:
        group, _ = Group.objects.get_or_create(name='Technicians')

        if not group.permissions.filter(codename='add_ticket').exists():
            add_ticket_permission = Permission.objects.get(codename='add_ticket')
            view_ticket_permission = Permission.objects.get(codename='view_ticket')
            group.permissions.add(add_ticket_permission, view_ticket_permission)

        instance.groups.add(group)