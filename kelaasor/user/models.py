from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission

class HeadMaster(AbstractUser):
    class Meta:
        verbose_name = 'HeadMaster'
        verbose_name_plural = 'HeadMasters'
    
    def has_perm(self, perm, obj= None):
        return True
    
    def has_perms(self, perm_list, obj = None):
        return True
    
    def has_module_perms(self, app_label):
        return True