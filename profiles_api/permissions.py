from rest_framework import  permissions


class UpdateOwnProfile(permissions.BasePermission):
    """allow user to edit their own profile"""

    def has_object_perrmission(self,request,view,obj):
        """check that user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id==request.user.id
