from rest_framework.permissions import BasePermission

class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and request.user.is_admin:
            return True
        
        return obj.user == request.user

class IsAdminOrOwner(BasePermission):
    def has_permission(self, request):
        return request.user.is_authenticated
    
    def has_object_permission(self, request,obj):
        if request.user.is_admin:
            return True
        return obj.user == request.user