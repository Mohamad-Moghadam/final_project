from rest_framework.permissions import BasePermission
from django.contrib.auth.models import Group, Permission


class IsHeadmaster(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name= "Headmaster").exists()


class IsTechnician(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name= "Technicians").exists()