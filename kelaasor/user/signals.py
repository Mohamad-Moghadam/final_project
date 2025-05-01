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

        for perm in custom_permissions:
            if not group.permissions.filter(id= perm.id).exists():
                group.permissions.add(perm)

        instance.groups.add(group)

    elif instance.is_staff and not instance.is_superuser:
        group, _ = Group.objects.get_or_create(name='Technicians')\
        
        custom_permissions= Permission.objects.filter(codename__in= ["add_responseticket", "view_responseticket", "delete_responseticket", "change_responseticket"])

        for perm in custom_permissions:
            if not group.permissions.filter(id= perm.id).exists():
                group.permissions.add(perm)

        instance.groups.add(group)