from rest_framework.permissions import BasePermission
from user.models import HeadMaster


class IsHeadmaster(BasePermission):
    def has_permission(self, request, view):
        return isinstance(self.user, HeadMaster)