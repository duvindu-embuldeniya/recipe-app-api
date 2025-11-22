from rest_framework import permissions


class UpdateOwnUser(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS: # GET and POST
            return True

        return obj.id == request.user.id
        #fields get dissapear