from rest_framework.permissions import BasePermission
from user.models import HeadMaster, Technicians


class IsHeadmaster(BasePermission):
    def has_permission(self, request, view):
        return isinstance(request.user, HeadMaster)


class IsTechnician(BasePermission):
    def has_permission(self, request, view):
        return isinstance(request.user, Technicians)