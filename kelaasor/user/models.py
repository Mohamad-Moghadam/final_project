from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models

class HeadMaster(AbstractUser):

    groups = models.ManyToManyField(
        Group,
        related_name='headmaster_users',
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='headmaster_user'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='headmaster_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='headmaster_user'
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