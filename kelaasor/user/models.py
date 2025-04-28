from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models


class DummyPermission(models.Model):
    class Meta:
        permissions= [("can_add_headmaster", "Can add headmaster"),
            ("can_list_headmasters", "Can list headmasters"),
            ("can_delete_headmaster", "Can delete headmaster"),
            ("can_retrieve_headmaster", "Can retrieve headmaster"),
            ("can_add_technician", "Can add technician"),
            ("can_list_technicians", "Can list technicians"),
            ("can_delete_technician", "Can delete technician"),
            ("can_retrieve_technician", "Can retrieve technician"),]

"""class HeadMaster(AbstractUser):

    groups = models.ManyToManyField(
        Group,
        related_name='headmaster_users',
        help_text='The groups this user belongs to.',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='headmaster_user_permissions',
        help_text='Specific permissions for this user.',
    )
    class Meta:
        verbose_name = 'HeadMaster'
        verbose_name_plural = 'HeadMasters'
    
    def has_perm(self, perm, obj= None):
        return True
    
    def has_perms(self, perm_list, obj = None):
        return True
    
    def has_module_perms(self, app_label):
        return True


class Technicians(AbstractUser):

    groups= models.ManyToManyField(
        Group,
        related_name='technician_users',
        help_text='The groups this user belongs to.',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='technician_user_permissions',
        help_text='Specific permissions for this user.',
    )
    class Meta:
        verbose_name= 'Technician'
        verbose_name_plural= 'Technicians'

    def has_perm(self, perm, obj= None):
        if perm in ['add_technician','change_technician','delete_technician']:
            return self.groups.filter(name='Technician').exists()
        return False"""