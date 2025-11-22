from rest_framework import permissions


class UpdateOwnRecipe(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user.id == request.user.id




class UpdateOwnTag(permissions.BasePermission):
    """Allow users to update their own status"""

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user.id == request.user.id
    


class UpdateOwnIngredient(permissions.BasePermission):
    """Allow users to update their own status"""

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user.id == request.user.id