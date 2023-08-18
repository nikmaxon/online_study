from rest_framework.permissions import BasePermission


class IsOwnerOrStaff(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return request.user == view.get_object().owner


class IsModerator(BasePermission):
    message = "У вас нет прав модератора!"

    def has_permission(self, request, view):
        if request.user.role == 'moderator':
            return True
        return False


class IsOwner(BasePermission):
    message = "У вас нет прав создателя!"

    def has_object_permission(self, request, view, object):
        if request.user == object.owner:
            return True
        return False


