from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models

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