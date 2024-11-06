from rest_framework import BasePermission



class IsProgrammes(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='programmes').exists()
