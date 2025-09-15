from rest_framework import permissions

class IsHost(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.host == request.user

class IsGuestOrListingHost(permissions.BasePermission):
    def has_permission(self, request, view, obj):
        isHost = obj.listing.host == request.user
        isGuest = obj.guest == request.user
        if request.method in permissions.SAFE_METHODS and isHost:
            return True
        return isGuest